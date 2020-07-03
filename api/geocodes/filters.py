import django_filters

from .models import GeoPoint


class GeoPointFilter(django_filters.FilterSet):
    class Meta:
        model = GeoPoint
        fields = [
            "latitude",
            "longitude",
            "street_number",
            "route",
            "neighborhood",
            "political",
            "administrative_area_level_1",
            "administrative_area_level_2",
            "country",
            "postal_code",
        ]
