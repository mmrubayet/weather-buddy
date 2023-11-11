import os
import json

from django.conf import settings
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response


from API.serializers import DistrictSerializer


class DistrictView(APIView):

    def get(self, request):
        static_file_path = os.path.join(
            settings.STATIC_ROOT, 'data/bd-districts.json'
        )

        # Load data from the JSON file
        with open(static_file_path) as f:
            district = json.load(f)
        return JsonResponse(district)
        