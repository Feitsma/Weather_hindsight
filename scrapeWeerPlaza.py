import pandas as pd
import datetime

weerplaza = pd.read_html('https://www.weerplaza.nl/nederland/eelde-paterswolde/8967/')

def getDate(combinedWeatherInfo):
    strings = combinedWeatherInfo.split(' ')
    date = strings[-1] + '-' + str(datetime.datetime.now().year)
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


week1 = weerplaza[1]
combinedWeatherInfo = week1[1]


date = getDate(combinedWeatherInfo[0])
T_max,T_min = getTemps(combinedWeatherInfo[2])
prec_prob = getPrec_prob(combinedWeatherInfo[3])
rain = getRain(combinedWeatherInfo[3])
windForce = getWind(combinedWeatherInfo[4])
