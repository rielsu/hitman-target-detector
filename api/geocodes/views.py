from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .filters import GeoPointFilter
from .models import GeoPoint
from .serializers import DecimalSerializer, GeoCodeSerializer
from .utils import calculate_euclidean_distance
from .webhooks import get_address_by_geolocation, get_geolocation_by_address


@api_view(["POST"])
def geolocation(request):
    data = request.data
    qs = GeoPoint.objects.all()
    geolocation = GeoPointFilter(data=data, queryset=qs, request=request).qs.first()
    if geolocation:
        serializer = GeoCodeSerializer(geolocation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    data = get_geolocation_by_address(*data.values())
    serializer = GeoCodeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def address(request):
    latitude = request.data.get("latitude")
    longitude = request.data.get("longitude")
    address = GeoPoint.objects.filter(latitude=latitude, longitude=longitude).first()
    if address:
        serializer = GeoCodeSerializer(address)
        return Response(serializer.data, status=status.HTTP_200_OK)

    address = get_address_by_geolocation(latitude, longitude)
    data = {"latitude": latitude, "longitude": longitude, **address}
    serializer = GeoCodeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def distance(request):
    params = request.query_params
    distance = calculate_euclidean_distance(
        **{key: tuple(value.split(",")) for key, value in params.items()}
    )
    serializer = DecimalSerializer(data=distance)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
