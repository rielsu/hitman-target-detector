import math
from decimal import Decimal, getcontext

from django.conf import settings


getcontext().prec = settings.DECIMAL_OPERATIONS_PRECISION


def calculate_euclidean_distance(start_point, end_point):
    quadratics = [
        (Decimal(start) - Decimal(end)) ** 2
        for start, end in zip(start_point, end_point)
    ]
    degrees = Decimal(math.sqrt(sum(quadratics)))
    distance = degrees * settings.GLOBAL_LONGITUDE_KM / settings.TOTAL_DEGREES
    miles = calculate_miles_from_kilometers(distance)
    return {"kilometers": round(distance, settings.DISTANCE_DECIMALS), **miles}


def calculate_miles_from_kilometers(distance):
    miles = round(distance / Decimal(settings.MILES_PER_KM), settings.DISTANCE_DECIMALS)
    return {"miles": miles}


def get_google_maps_api_address_components(response):
    components = response["results"][0]["address_components"]
    components = {
        component["types"][0]: component["long_name"] for component in components
    }
    return {**components}


def get_google_maps_api_location(response):
    location = response["results"][0]["geometry"]["location"]
    location = {
        "latitude": round(Decimal(location["lat"]), settings.GEOPOINT_DECIMAL_PLACES),
        "longitude": round(Decimal(location["lng"]), settings.GEOPOINT_DECIMAL_PLACES),
    }
    components = response["results"][0]["address_components"]
    components = {
        component["types"][0]: component["long_name"] for component in components
    }
    return {**components, **location}
