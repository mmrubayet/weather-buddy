from django.urls import path

from .views import DistrictView

urlpatterns = [
    path("districts/", DistrictView.as_view(), name="districts"),
]
