from django.contrib import admin
from maps.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'lat',
        'lon',
        'address'
    )
    search_fields = ['address']

admin.site.register(Location, LocationAdmin)
