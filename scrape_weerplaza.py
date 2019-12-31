"""
Scrapes weerplaze.nl for the location Eelde and retrieves the prediction for 14 days.
the predictions are stored in a database to preform a quality check with the actual weather
"""

import pandas as pd
import datetime
import addDB


def get_date(combined_weather_info):
    strings = combined_weather_info.split(' ')
    date = strings[-1] + '-' + str(datetime.datetime.now().year)
    date = datetime.datetime.strptime(date, '%d-%m-%Y') # TODO fix end of year bug where for the first to weeks of jan the year is not correct.
    return date


def get_temps(combined_weather_info):
    strings = combined_weather_info.split(' ')
    t_max = strings[0]
    t_min = strings[2]
    return t_max, t_min

def get_prec_prob(combined_weather_info):
    strings = combined_weather_info.split(' ')
    prec_prob = strings[0]
    prec_prob = prec_prob.replace('%', '')
    prec_prob = int(prec_prob)/100
    return prec_prob

def get_rain(combined_weather_info):
    strings = combined_weather_info.split(' ')
    rain = strings[2]
    rain = rain.replace(',', '.')
    return rain

def get_wind(combined_weather_info):
    strings = combined_weather_info.split(' ')
    wind_force = strings[-1]
    return wind_force

def get_wind_direction(combined_weather_info):
    strings = combined_weather_info.split(' ')
    wind_direction = strings[0]
    return wind_direction

def loop_through_days(weatherdata,prediction_in_days):

    for day in [0,2,4,6,8,10,12]:
        weatheroftheday = weatherdata[day]

        date = get_date(weatheroftheday[0])
        t_max,t_min = get_temps(weatheroftheday[2])
        prec_prob = get_prec_prob(weatheroftheday[3])
        rain = get_rain(weatheroftheday[3])
        wind_force = get_wind(weatheroftheday[4])
        wind_direction = get_wind_direction(weatheroftheday[4])

        addDB.add('prediction', date, t_max, t_min, prec_prob, rain, wind_force, wind_direction, prediction_in_days)
        prediction_in_days = prediction_in_days + 1


weerplaza = pd.read_html('https://www.weerplaza.nl/nederland/eelde-paterswolde/8967/')

#Prediction for x days in advance
prediction_in_days = 1
#Week1
loop_through_days(weerplaza[1], prediction_in_days)

#Prediction for x days in advance
prediction_in_days = 8
#Week2
loop_through_days(weerplaza[9], prediction_in_days)


