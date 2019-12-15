import pandas as pd
import numpy as np
import dbsettings
import datetime
import mysql.connector


datum = datetime.datetime.now()
dag = int(datum.strftime("%d"))
dag_gisteren = dag-1
weerstatistieken = pd.read_html(io='https://weerstatistieken.nl/eelde', decimal=',', thousands='.')
temperaturen = weerstatistieken[0] #pak de tabel met temperatuurdata
vandaag = temperaturen.iloc[dag_gisteren] #vandaag is het de 14e, maar 13 ivm python indexing
max = float(vandaag[2]) #max temperatuur vandaag
min = float(vandaag [1])


conn = mysql.connector.connect(user= dbsettings.user, password = dbsettings.password, database=dbsettings.database, host=dbsettings.host)
cursor = conn.cursor()

sql = "INSERT INTO t (DateTime, T_max, T_min) VALUES (%s, %s, %s)"
val = (datum, max, min)

cursor.execute(sql, val)

conn.commit()
cursor.close()
conn.close()