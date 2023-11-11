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
        "weather/cool/",
        views.CoolWeather.as_view(),
        name="cool_weather"
    ),
]
