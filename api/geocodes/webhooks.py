import requests
from django.conf import settings

from .utils import get_google_maps_api_address_components, get_google_maps_api_location


def get_address_by_geolocation(*args):
    payload = {"key": settings.GOOGLE_MAPS_API_KEY, "latlng": ",".join(args)}
    response = requests.get(settings.GOOGLE_MAPS_API_ENDPOINT, params=payload)
    json = response.json()
    if json["status"] == "REQUEST_DENIED":
        raise Exception(json["error_message"])
    return get_google_maps_api_address_components(json)


def get_geolocation_by_address(*args):
    payload = {"key": settings.GOOGLE_MAPS_API_KEY, "address": "+".join(args)}
    response = requests.get(settings.GOOGLE_MAPS_API_ENDPOINT, params=payload)
    json = response.json()
    if json["status"] == "REQUEST_DENIED":
        raise Exception(json["error_message"])
    return get_google_maps_api_location(json)
