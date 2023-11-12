
from rest_framework.views import APIView, Response

from weathers.models import District

from weathers.helpers import (
    get_temperature,
    get_cool_ten_districts,
    compare_temperature,
    is_valid_date
)


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
    Returns Top Ten Cool Districts Based on Weather
    for Next 7 Days of 64 Districts.
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


class TravelToCool(APIView):
    """
    Takes Current and Desired Location with date and
    Returns is Cooler or Not.
    """

    def get(self, request, format=None):

        from_id = request.query_params.get("from_id")
        to_id = request.query_params.get("to_id")
        date = request.query_params.get("date")

        if int(from_id) in range(1, 65):
            current_location = District.objects.filter(dist_id=from_id).first()
        else:
            return Response({
                "message": "Invalid Query Data. from_id not found"
            }, status=400)

        if int(to_id) in range(1, 65):
            desired_location = District.objects.filter(dist_id=to_id).first()
        else:
            return Response({
                "message": "Invalid Query Data. to_id not found"
            }, status=400)

        if date and not is_valid_date(date):
            return Response({
                "message": "Please check date format. Desired '%Y-%m-%d'"
            }, status=400)

        district = [current_location.name, desired_location.name]
        lat = [float(current_location.lat), float(desired_location.lat)]
        long = [float(current_location.long), float(desired_location.long)]
        temp_list = compare_temperature(district, lat, long, date)
        return Response(temp_list, status=200)
