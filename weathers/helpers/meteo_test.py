import numpy as np
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

# Set up the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession(
    '.cache', expire_after=3600
)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
open_meteo = openmeteo_requests.Client(session=retry_session)


# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important
# to assign them correctly below

url = "https://api.open-meteo.com/v1/forecast"


def get_hour_temp(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }
    responses = open_meteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple
    # locations or weather models
    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")  # noqa
    # print(f"Elevation {response.Elevation()} m asl")

    # Process hourly data. The order of variables
    # needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s"),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ),
        "temperature_2m": hourly_temperature_2m}

    hdf = pd.DataFrame(data=hourly_data)

    # Extract data from the JSON response
    dates = pd.to_datetime(hdf["date"], format="%Y-%m-%dT%H:%M:%S")
    temperature_2m = np.array(hdf["temperature_2m"])

    # Create a DataFrame
    hourly_data = {"date": dates, "temperature_2m": temperature_2m}
    hourly_df = pd.DataFrame(data=hourly_data)

    # Filter the DataFrame for entries where the time is 2:00 PM
    filtered_df = hourly_df[hourly_df['date'].dt.hour == 14]
    result_dict = dict(
        zip(
            filtered_df['date'].dt.day,
            filtered_df['temperature_2m']
        )
    )

    # Print the filtered DataFrame
    # print(result_dict)

    return result_dict
