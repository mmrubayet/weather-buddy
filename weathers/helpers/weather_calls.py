
from .meteo_response import get_response, parse_response
from .utils import get_named_temp, get_average_temp, get_top_ten, get_day


def get_temperature(districts, latitude, longitude, date=None):

    # Get district temperature response
    responses = get_response(latitude, longitude, date)
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


def compare_temperature(districts, latitude, longitude, date):

    # Get district temperature
    dt = get_temperature(districts, latitude, longitude, date)

    day = get_day(date)

    if dt[districts[0]][day] < dt[districts[1]][day]:
        decision = f"{districts[1]} is hot than you are in {districts[0]}. "\
                   f"You should not go there."

    elif dt[districts[0]][day] > dt[districts[1]][day]:
        decision = f"{districts[1]} is cool than you are in {districts[0]}. "\
                   "Go Enjoy!"

    elif dt[districts[0]][day] < dt[districts[1]][day]:
        decision = f"{districts[1]} is same as you are in {districts[1]}."

    else:
        decision = "Can't decide."

    dt["decision"] = decision

    return dt
