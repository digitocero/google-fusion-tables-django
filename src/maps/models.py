from django.db import models
from django.conf import settings

from httplib2 import Http
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class Location(models.Model):
    # at least 15 decimal places are seen regularly
    lat = models.DecimalField(max_digits=40, decimal_places=30)
    lon = models.DecimalField(max_digits=40, decimal_places=30)
    address = models.TextField(max_length=200)

    def add(self, lat, lon, address):
        print(lat, lon, address)
        Location.objects.create(
            lat=lat,
            lon=lon,
            address=address
        )

    def exists(self, lat, lon, address):
        return Location.objects.filter(
            lat=lat,
            lon=lon,
            address=address
        ).exists()

    def get_all(self):
        return Location.objects.all()

    def delete_all(self):
        return Location.objects.all().delete()


class FusionLocation():
    """
    The google fusion table
    """
    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/fusiontables']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            settings.SERVICE_ACCOUNT_KEY_PATH,
            scopes=scopes
        )

        # httplib2.debuglevel = 1
        http_auth = credentials.authorize(Http())
        resource = build("fusiontables", "v2", http=http_auth)
        conn = resource.query()

        self.conn = conn

    def get_all(self):
        # return []
        """
        explicit values query and return
        otherwise they are positional
        """
        sql = "SELECT lat,lon, address FROM {table_name}".format(
            table_name=settings.FUSION_TABLE_NAME
        )
        items = self.conn.sql(sql=sql).execute()
        for item in items['rows']:
            yield {
                'lat': item[0],
                'lon': item[1],
                'address': item[2],
            }
        return items

    def add(self, lat, lon, address):
        # query is sensitive to newlines
        sql = """
            INSERT INTO {table_name} (lat, lon, address) 
            VALUES ({lat}, {lon}, '{address}')
        """.format(
            table_name=settings.FUSION_TABLE_NAME,
            lat=lat,
            lon=lon,
            address=address,
        ).strip()
        self.conn.sql(sql=sql).execute()

    def delete_all(self):
        sql = "DELETE FROM {table_name}".format(
            table_name=settings.FUSION_TABLE_NAME
        )
        self.conn.sql(sql=sql).execute()

