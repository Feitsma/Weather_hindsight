import pandas as pd
import addDB

#Makkelijk te scrapen
weerplaza = pd.read_html('https://www.weerplaza.nl/nederland/delfzijl/8570/')
print(weerplaza[1][8])

weerDezeWeek = weerplaza[1]
weerVolgendeWeek = weerplaza[9]

#KNMI DATA
#http://projects.knmi.nl/klimatologie/daggegevens/selectie.cgi
#http://projects.knmi.nl/klimatologie/daggegevens/getdata_dag.cgi?lang=nl&byear=2019&bmonth=10&bday=9&eyear=2019&emonth=10&eday=9&variabele=DDVEC&variabele=TX&variabele=T10N&variabele=RH&variabele=UG&stations=280&submit=Download+data+set