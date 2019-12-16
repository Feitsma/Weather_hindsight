#import wget
import knmi
import pandas as pd
import datetime

#url = "http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi/&stns=235:280:260&vars=VICL:PRCP&byear=1970&bmonth=1&bday=1&eyear=2009&emonth=8&eday=18"
#wget.download(url)

#Get the date of yesterday to retreive its information from KNMI
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')

#dag = int(datum.strftime("%d"))
#maand = int(datum.strftime("%m"))
#jaar = int(datum.strftime("%Y"))
#end = '{}{}{}'.format(jaar,maand,dag)

#Station 280 is Eelde
df = knmi.get_day_data_dataframe(start=yesterday,stations=[280])

#print(df.disclaimer)
#print(df.stations)
#print(df.legend)
#df = df.rename(columns=df.legend)
print(df)
variables = knmi.variables
min_temp = df['TN'].iloc[-1]/10 #min. temp tijdens laatste entry (moet gisteren zijn)
max_temp = df['TX'].iloc[-1]/10 #max. temp
rain = df['RH'].iloc[-1]/10 #rain
