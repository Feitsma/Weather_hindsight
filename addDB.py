import mysql.connector
import dbsettings

conn = mysql.connector.connect(user= dbsettings.user, password = dbsettings.password, database=dbsettings.database, host=dbsettings.host)
cursor = conn.cursor()

weatherForT = 't1'

def add(weatherForT):
    add_positionlog = ("INSERT INTO " + weatherForT + " (DateTime,T_max,T_min,prec_prob,mm,wind) VALUES (%(DateTime)s, %(T_max)s, %(T_min)s, %(prec_prob)s,%(mm)s,%(wind)s)")
    data_position = {
    'DateTime': '3',
    'T_max': '50000',
    'T_min': '1',
    'prec_prob': '3',
    'mm': '5',
    'wind': '6',
    }

    cursor.execute(add_positionlog,data_position)
    conn.commit()
    cursor.close()
    conn.close()


add('t1')