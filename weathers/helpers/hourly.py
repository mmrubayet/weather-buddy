
import pandas as pd
import numpy as np

from .meteo import open_meteo, url


def get_response(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m"]
    }
    print(params)
    responses = open_meteo.weather_api(url, params=params)

    return responses


def parse_response(responses):

    result_obj = []
    for response in responses:
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
        # print(hdf)

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
        result_obj.append(result_dict)

    # print(f"result_obj: {result_obj}")
    return result_obj


def get_temperature(latitude, longitude):
    responses = get_response(latitude, longitude)
    return parse_response(responses)
