from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^distance/", views.distance, name="calculate_distance"),
    url(r"^address/", views.address, name="address"),
    url(r"^geolocation/", views.geolocation, name="address"),
]
