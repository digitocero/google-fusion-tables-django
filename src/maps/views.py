from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from maps.models import Location, FusionLocation
from decimal import Decimal


def index(request):
    fusion_locations = FusionLocation().get_all()

    # make sure all the fusion one exists locally
    for loc in fusion_locations:
        if not Location().exists(loc['lat'], loc['lon'], loc['address']):
            Location().add(loc['lat'], loc['lon'], loc['address'])

    context = {
        'locations': fusion_locations,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_API_KEY,
        'FUSION_TABLE_NAME': settings.FUSION_TABLE_NAME
    }
    return render(request, 'base.html', context)


"""
REST API
"""


def location_post(request):
    """
    add a new location, unless it already exists
    only POST or method not supported
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    lat = request.POST.get('lat', '')
    lon = request.POST.get('lon', '')
    address = request.POST.get('address', '')

    if not lat or not lon or not address:
        # invalid request
        return HttpResponse(status=400)

    lat = Decimal(lat)
    lon = Decimal(lon)

    # no duplicates
    if not Location().exists(lat, lon, address):
        Location().add(lat, lon, address)
        FusionLocation().add(str(lat), str(lon), address)

    return HttpResponse('ok')

def reset_post(request):
    """
    Reset all the data
    only POST or method not supported
    """
    if request.method != 'POST':
        return HttpResponse(status=405)

    Location().delete_all()
    FusionLocation().delete_all()

    return HttpResponse('ok')
