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

week1 = weerplaza[1]
combinedWeatherInfo = week1[1]


date = getDate(combinedWeatherInfo[0])
T_max,T_min = getTemps(combinedWeatherInfo[2])