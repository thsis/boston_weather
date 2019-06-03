"""
Obtain weather data from 2001-2008 for Boston Airport.

This script scrapes the web for weather data, interfacing with the Dark Sky API
in order to obtain data about temperature and weather conditions measured at
Boston Logan International Airport. At the end you will write a `csv-file` to
the `data` directory of this repository (on your local disk, of course).
"""

import os
import warnings
import requests
import pandas as pd
import numpy as np
from darksky import forecast
from datetime import datetime
from tqdm import tqdm


def ping_darksky(time, key):
    """
    Interface to Dark Sky API. Requests data from Boston Airport for a specific
    time.

    * Arguments:
        + time: a datetime object. Denotes the day of the requested record.
        + key: a character string. Key to interface the Dark Sky API.

    * Returns:
        + Dictionary containing:
            + day: datetime of the observation (in timestamp format).
            + tempMin: minimum temperature in degrees Fahrenheit at that date.
            + tempMax: maximum temperature in degrees Fahrenheit at that date.
            + summary: weather summary of that date.
            + desc: single word description of weather conditions.
            + cloud_cover: float denoting the proportion of the skies surface
              that is obscured by clouds

    """
    boston = forecast(key, *BOSTON, time=time.isoformat())

    fetch = {
        'day': time,
        'tempMin': boston["daily"]["data"][0].get('temperatureMin', np.nan),
        'tempMax': boston["daily"]["data"][0].get('temperatureMax', np.nan),
        'summary': boston["daily"]["data"][0].get('summary', np.nan),
        'desc': boston["daily"]["data"][0].get('icon', np.nan),
        'cloudCover': boston["daily"]["data"][0].get('cloudCover', np.nan)}
    return fetch


def switch_key():
    """
    Key generator that allows to switch between keys that are provided in the
    `secret_key.txt` file.

    * Yields:
        + Key to access Dark Sky API.
    """
    with open("secret_key.txt", 'r') as key_file:
        api_keys = key_file.read().splitlines()

    for api_key in api_keys:
        yield api_key


# Define location.
BOSTON = (42.3601, -71.0589)
# Set up dataframe and path to which it will be saved.
COLUMNS = ["day", "tempMin", "tempMax", "summary", "desc", "cloudCover"]
WEATHER_BOSTON = pd.DataFrame(columns=COLUMNS)
DATAOUT = os.path.join("data", "weather_boston_daily.csv")
# Define start variables for the loop.
START = datetime(2001, 1, 1, 12)
KEYGEN = switch_key()
KEY = next(KEYGEN)

if __name__ == "__main__":
    print("Start data collection.")
    for day in tqdm(pd.date_range(START, periods=4050)):
        try:
            row = ping_darksky(key=KEY, time=day)
            WEATHER_BOSTON = WEATHER_BOSTON.append(row, ignore_index=True)
        # If the server refuses to connect, change the key.
        except requests.exceptions.HTTPError:
            try:
                KEY = next(KEYGEN)
                row = ping_darksky(key=KEY, time=day)
                WEATHER_BOSTON = WEATHER_BOSTON.append(row, ignore_index=True)
                continue
            # If there are no keys left, break the loop prematurely.
            except StopIteration:
                warnings.warn(
                    "End of keys reached. Your dataset might be incomplete.")
                break
        # Save data in each iteration.
        # This way you should end up with something at least.
        finally:
            WEATHER_BOSTON.to_csv(DATAOUT)

    print("Wrote {} rows".format(WEATHER_BOSTON.shape[0]))


fetch
