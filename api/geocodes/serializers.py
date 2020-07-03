from rest_framework import serializers

from .models import GeoPoint


# Serializers define the API representation.
class GeoCodeSerializer(serializers.ModelSerializer):
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
            "formatted_address",
        ]


class DecimalSerializer(serializers.Serializer):
    kilometers = serializers.DecimalField(max_digits=8, decimal_places=3)
    miles = serializers.DecimalField(max_digits=8, decimal_places=3)
