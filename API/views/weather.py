
from rest_framework.views import APIView, Response

from weathers.models import District

from weathers.helpers import get_temperature, get_cool_ten_districts


class Weather7d64D(APIView):
    """
    Returns Weather for 7 days 64 districts
    """

    def get(self, request, format=None):

        obj_list = list(District.objects.values_list(
            "name", "lat", "long"
        ))
        district = list()
        lat = list()
        long = list()
        for obj in obj_list:
            district.append(obj[0])
            lat.append(float(obj[1]))
            long.append(float(obj[2]))
        temp_list = get_temperature(district, lat, long)
        return Response(temp_list, status=200)


class CoolWeatherTopTen(APIView):
    """
    Returns Top Ten Cool Districts Based on Weather for Next 7 Days of 64 Districts.
    """

    def get(self, request, format=None):

        obj_list = list(District.objects.values_list(
            "name", "lat", "long"
        ))
        district, lat, long = list(), list(), list()
        for obj in obj_list:
            district.append(obj[0])
            lat.append(float(obj[1]))
            long.append(float(obj[2]))
        temp_list = get_cool_ten_districts(district, lat, long)
        return Response(temp_list, status=200)
