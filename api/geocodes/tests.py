from rest_framework.test import RequestsClient
from django.test import TestCase


class GeoCodeTestCase(TestCase):
    
    def test_geocodes_distance(self):
        client = RequestsClient()
        response = client.get(
            "http://localhost:8000/geocodes/distance?start_point=2.3321, -13.3312&end_point=2.3321, -13.33"
        )
        json = response.json()
        assert response.status_code == 200
        assert json["kilometers"] == "0.134"
        assert json["miles"] == "0.083"

    def test_geocodes_geolocation(self):
        client = RequestsClient()
        data = {
            "street_number": "144",
            "route": "Boldo",
            "neighborhood": "",
            "political": "Victoria de las Democracias",
        }
        response = client.post("http://localhost:8000/geocodes/geolocation/", data=data)
        json = response.json()
        assert response.status_code == 201
        assert json["latitude"] == "19.46896670"
        assert json["longitude"] == "-99.16616770"

    def test_geocodes_address(self):
        client = RequestsClient()
        data = {"latitude": "40.714", "longitude": "-73.961452"}
        response = client.post("http://localhost:8000/geocodes/address/", data=data)
        json = response.json()
        assert response.status_code == 201
        assert json["street_number"] == "287"
        assert json["route"] == "Bedford Avenue"
        assert json["neighborhood"] == "Williamsburg"
        assert json["political"] == "Brooklyn"
        assert json["administrative_area_level_1"] == "New York"
        assert json["administrative_area_level_2"] == "Kings County"
        assert json["country"] == "United States"
        assert json["postal_code"] == "11211"
        assert (
            json["formatted_address"]
            == "287 Bedford Avenue Williamsburg Brooklyn, New York Kings County 11211, United States"
        )
