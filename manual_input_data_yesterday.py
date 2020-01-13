import knmi
import converter_functions
import datetime
import addDB

"""This script is for manual input into the database, if for whatever reason a data point was not recorded"""

#Get the date of yesterday to retreive its information from KNMI
start = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
stop = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')

#Station 280 is Eelde
df = knmi.get_day_data_dataframe(stations=[280], start=start, end=stop)
variables = knmi.variables #Gives a list of all callable variables in this API
min_temp = float(df['TN'].iloc[-1]/10) #min. temp of most recent entry, should be yesterday
max_temp = float(df['TX'].iloc[-1]/10) #max. temp
rain = float(df['RH'].iloc[-1]/10) #rain (is -0.1 if it only rained a little bit, according to KNMI)
if rain == -0.1: #in order to show that it has rained but just a little bit.
    rain = 0.01
wind_speed = df['FG'].iloc[-1]/10 #mean windspeed (m/s)
Beaufort = converter_functions.meteric_to_Beaufort(wind_speed) #call conververt function
wind_direction = int(df['DDVEC'].iloc[-1]) #wind direction (360=north, 90=east, 180=south, 270=west, 0=calm/variable)
direction_text = converter_functions.wind_direction_to_text(wind_direction) #call converter function

#add to database
addDB.add_data_yesterday(start, max_temp, min_temp, rain, Beaufort, direction_text)