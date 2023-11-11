from rest_framework import serializers


class DistrictSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    division_id = serializers.IntegerField()
    name = serializers.CharField()
    bn_name = serializers.CharField()
    lat = serializers.CharField()
    long = serializers.CharField()
