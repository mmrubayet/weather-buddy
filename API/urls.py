from django.urls import path

from . import views

urlpatterns = [
    path(
        "districts/",
        views.DistrictListCreateView.as_view(),
        name="district_list_create"
    ),
    path(
        "districts/<int:dist_id>/",
        views.DistrictRetrieveUpdateDestroyView.as_view(),
        name="district_retrieve_update_destroy"
    ),
    path(
        "districts/travel/cool/",
        views.TravelToCool.as_view(),
        name="cool_ten"
    ),
    path(
        "districts/travel/cool/rt/",
        views.TravelToCoolRT.as_view(),
        name="cool_ten_rt"
    ),
    path(
        "districts/weather/temperature/",
        views.Weather7d64D.as_view(),
        name="districts_temperature"
    ),
    path(
        "districts/weather/cool-ten/",
        views.CoolWeatherTopTen.as_view(),
        name="cool_ten"
    ),
]
