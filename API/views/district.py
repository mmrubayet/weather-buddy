
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from API.serializers import DistrictSerializer
from weathers.models import District


class DistrictListCreateView(ListCreateAPIView):

    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class DistrictRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = "dist_id"
