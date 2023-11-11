from django.db import models


class DistrictManager(models.Manager):
    pass


class District(models.Model):
    dist_id = models.PositiveIntegerField(null=True, blank=True)
    division_id = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    bn_name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    objects = DistrictManager()

    def __str__(self):
        return f"{self.name} ({self.dist_id}) - {self.division_id}"
