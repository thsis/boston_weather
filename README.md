# Scraping Weather Data for Boston MA from Dark Sky

[Powered By Dark Sky](https://darksky.net/poweredby/)

This script scrapes the web for weather data, interfacing with the Dark Sky API
in order to obtain data about temperature and weather conditions measured at
Boston Logan International Airport. At the end you will write a `csv-file` to
the `data` directory of this repository (on your local disk, of course).

The contents of `weather_boston_daily.csv` are 4004 rows of observations for:

* `day`: datetime of the observation (in timestamp format).
* `tempMin`: minimum temperature in degrees Fahrenheit at that date.
* `tempMax`: maximum temperature in degrees Fahrenheit at that date.
* `summary`: weather summary of that date.
* `desc`: single word description of weather conditions.
* `cloud_cover`: float denoting the proportion of the skies surface that is obscured by clouds


## Getting started with Python
Download and install `Python3.6` from https://www.python.org/downloads/. Make sure to include it to your `PATH` variable if you are using `Windows` or `MacOS` (just tick the box during the installation).

To run the `Python` code from this repository you may need to install additional modules. You can do this by opening a terminal (`CTRL-ALT-T` on `Linux` or `MacOS`) or a command line (on `Windows` just push `HOME` and start typing `run`, you should see a black icon, click that to enter `PowerShell`).

First you want to change into your directory:
```
cd __path_to_your_cloned_repository__
```
Next you want to install the packages from the `requirements.txt`-file:
```
pip install -r requirements.txt
```

Thats all. After that you can run the python scripts by running:
```
python __name_of_script__.py
```
Note that this might be different if you are using `IDE`'s like `PyCharm`, `IDLE`, `Spyder`, etc.


## Running this script

1. Get a key from https://darksky.net/dev.
2. install the `darksky`-module from github, since this seems to be the only version that, at the time of writing this, is not broken:
```
pip install git+https://github.com/zachwill/darksky.git --user
```
3. Save your key in the `key.txt`-file. Of course I highly discourage to **add multiple keys** from different people to circumvent the access limitations for free users.
4. run the `weather.py` script.

<h2 id="weather">weather</h2>
<h3 id="weather.ping_darksky">ping_darksky</h3>

```python
ping_darksky(time, key)
```

Interface to Dark Sky API. Requests data from Boston Airport for a specific
time.

* Arguments:
    + `time`: a datetime object. Denotes the day of the requested record.
    + `key`: a character string. Key to interface the Dark Sky API.

* Returns:
    + Dictionary containing:
        + `day`: datetime of the observation (in timestamp format).
        + `tempMin`: minimum temperature in degrees Fahrenheit at that date.
        + `tempMax`: maximum temperature in degrees Fahrenheit at that date.
        + `summary`: weather summary of that date.
        + `desc`: single word description of weather conditions.
        + `cloud_cover`: float denoting the proportion of the skies surface that is obscured by clouds


<h3 id="weather.switch_key">switch_key</h3>

```python
switch_key()
```

Key generator that allows to switch between keys that are provided in the
`secret_key.txt` file.

* Yields:
    + Key to access Dark Sky API.
