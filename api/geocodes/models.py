"""Django models utilities."""

# Django
from django.db import models
from django.conf import settings


class TemplateModel(models.Model):
    """ Manager base model."""

    created = models.DateTimeField(
        "created at",
        auto_now_add=True,
        help_text="Date time on which the object was created.",
    )
    modified = models.DateTimeField(
        "modified at",
        auto_now=True,
        help_text="Date time on which the object was last modified.",
    )

    class Meta:
        """Meta option."""

        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-modified"]


class GeoPoint(TemplateModel):
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=settings.GEOPOINT_DECIMAL_PLACES,
        blank=True,
        null=True,
    )
    longitude = models.DecimalField(
        max_digits=11,
        decimal_places=settings.GEOPOINT_DECIMAL_PLACES,
        blank=True,
        null=True,
    )
    street_number = models.CharField(blank=True, null=True, max_length=50)
    route = models.CharField(blank=True, null=True, max_length=50)
    neighborhood = models.CharField(blank=True, null=True, max_length=50)
    political = models.CharField(blank=True, null=True, max_length=50)
    administrative_area_level_1 = models.CharField(blank=True, null=True, max_length=50)
    administrative_area_level_2 = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)
    postal_code = models.CharField(blank=True, null=True, max_length=10)

    @property
    def formatted_address(self):
        return "{street_number} {route} {neighborhood} {political}, {administrative_area_level_1} {administrative_area_level_2} {postal_code}, {country}".format(
            street_number=self.street_number or "",
            route=self.route or "",
            neighborhood=self.neighborhood or "",
            political=self.political or "",
            administrative_area_level_1=self.administrative_area_level_1 or "",
            administrative_area_level_2=self.administrative_area_level_2 or "",
            country=self.country or "",
            postal_code=self.postal_code or "",
        )

    def __str__(self):
        """Return details."""
        return "created at {created} postiion  {latitude} | {longitude} ".format(
            created=self.created, latitude=self.latitude, longitude=self.longitude,
        )
