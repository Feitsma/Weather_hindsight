import knmi
import pandas as pd
import wind_Converter
import datetime
import addDB

#Get the date of yesterday to retreive its information from KNMI
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
#Station 280 is Eelde
df = knmi.get_day_data_dataframe(stations=[280], start=yesterday)
variables = knmi.variables #handig als je wilt weten wat je allemaal kunt oproepen van KNMI
print(variables)
min_temp = float(df['TN'].iloc[-1]/10) #min. temp tijdens laatste entry (moet gisteren zijn)
max_temp = float(df['TX'].iloc[-1]/10) #max. temp
rain = float(df['RH'].iloc[-1]/10) #rain
wind_speed = df['FG'].iloc[-1]/10 #mean windspeed (m/s)
Beaufort = wind_Converter.meteric_to_Beaufort(wind_speed)
wind_direction = int(df['DDVEC'].iloc[-1]) #wind direction (360=north, 90=east, 180=south, 270=west, 0=calm/variable)

#add to database
addDB.add_data_yesterday(yesterday, max_temp, min_temp, rain, Beaufort, wind_direction)

