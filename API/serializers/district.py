from rest_framework import serializers

from weathers.models import District


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        exclude = ["id"]
