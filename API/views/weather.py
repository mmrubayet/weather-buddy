
from rest_framework.views import APIView, Response

from weathers.models import District

from weathers.opm import get_hour_temp


class CoolWeather(APIView):

    def get(self, request, format=None):

        obj_list = list(District.objects.values_list(
            "name", "lat", "long"
        ))
        temp_list = list()

        for obj in obj_list:
            temp = dict()
            temp["district"] = obj[0]
            temp["temp"] = get_hour_temp(obj[1], obj[2])
            temp_list.append(temp)

        return Response(temp_list, status=200)
