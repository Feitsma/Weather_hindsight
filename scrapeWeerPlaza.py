"""
Scrapes weerplaze.nl for the location Eelde and retrieves the prediction for 14 days.
The predictions are stored in a database to preform a quality check with the actual weather
"""

import pandas as pd
import datetime
import addDB

weerplaza = pd.read_html('https://www.weerplaza.nl/nederland/eelde-paterswolde/8967/')

def getDate(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    date = strings[-1] + '-' + str(datetime.datetime.now().year)
    date = datetime.datetime.strptime(date, '%d-%m-%Y')
    return date


def getTemps(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    T_max = strings[0]
    T_min = strings[2]
    return T_max,T_min

def getPrec_prob(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    prec_prob = strings[0]
    prec_prob = prec_prob.replace('%', '')
    prec_prob = int(prec_prob)/100
    return prec_prob

def getRain(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    rain = strings[2]
    rain = rain.replace(',', '.')
    return rain

def getWind(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    windForce = strings[-1]
    return windForce


def loopThroughDays(weatherdata,prediction_in_days):

    for day in [0,2,4,6,8,10,12]:
        weatheroftheday = weatherdata[day]

        date = getDate(weatheroftheday[0])
        T_max,T_min = getTemps(weatheroftheday[2])
        prec_prob = getPrec_prob(weatheroftheday[3])
        rain = getRain(weatheroftheday[3])
        windForce = getWind(weatheroftheday[4])

        addDB.add('prediction', date, T_max, T_min, prec_prob, rain, windForce,prediction_in_days)

        prediction_in_days = prediction_in_days + 1

#Prediction for x days in advance
prediction_in_days = 1
#Week1
loopThroughDays(weerplaza[1],prediction_in_days)

#Prediction for x days in advance
prediction_in_days = 8
#Week2
loopThroughDays(weerplaza[9],prediction_in_days)


