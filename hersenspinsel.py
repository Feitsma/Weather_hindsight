import pandas as pd
import numpy as np

#Makkelijk te scrapen
weerplaza = pd.read_html('https://www.weerplaza.nl/nederland/delfzijl/8570/')
print(weerplaza[1][8])


#Deze is een motherfucker
#yahoo = pd.read_html('https://weather.com/weather/tenday/l/fa52f9623f642373090acc26649060007bf682b7a41c7c99e2d3c1d2aba9c7cc')



#buienradar = pd.read_html('https://www.buienradar.nl/weer/delfzijl/nl/2757340/14daagse')

#Veertien daagse voorspelling


#KNMI DATA
#http://projects.knmi.nl/klimatologie/daggegevens/selectie.cgi
#http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi?lang=nl&byear=2019&bmonth=10&bday=9&eyear=2019&emonth=10&eday=9&variabele=DDVEC&variabele=TX&variabele=T10N&variabele=RH&variabele=UG&stations=280&submit=Download+data+set