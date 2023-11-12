
from .meteo_response import get_response, parse_response
from .utils import get_named_temp, get_average_temp, get_top_ten


def get_temperature(districts, latitude, longitude):

    # Get district temperature response
    responses = get_response(latitude, longitude)
    # Format response
    temp_2pm_7d = parse_response(responses)
    # Add names with district temperature
    district_temp = get_named_temp(districts, temp_2pm_7d)
    return district_temp


def get_cool_ten_districts(districts, latitude, longitude):

    # Get district temperature
    district_temp = get_temperature(districts, latitude, longitude)
    # Calculate average district temperature
    average_dist_temp = get_average_temp(district_temp)
    # Get top ten district based on low temperature
    top_ten_cool = get_top_ten(average_dist_temp)

    return top_ten_cool
