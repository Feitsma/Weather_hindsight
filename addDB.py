import mysql.connector
import dbsettings



def add(table,day,T_max,T_min,prec_prob,mm,wind,prediction_in_days):
    conn = mysql.connector.connect(user=dbsettings.user, password=dbsettings.password, database=dbsettings.database,
                                   host=dbsettings.host)
    cursor = conn.cursor()
    add_positionlog = ("INSERT INTO " + table + " (prediction_for,T_max,T_min,prec_prob,mm,wind,prediction_in_days) VALUES (%(prediction_for)s, %(T_max)s, %(T_min)s, %(prec_prob)s,%(mm)s,%(wind)s,%(prediction_in_days)s)")
    data_position = {
    'prediction_for': day,
    'T_max': T_max,
    'T_min': T_min,
    'prec_prob': prec_prob,
    'mm': mm,
    'wind': wind,
    'prediction_in_days': prediction_in_days,
    }

    cursor.execute(add_positionlog,data_position)
    conn.commit()
    cursor.close()
    conn.close()

def add_data_yesterday(date_yesterday, max_temp, min_temp, rain, Beaufort, wind_direction):
    conn = mysql.connector.connect(user=dbsettings.user, password=dbsettings.password, database=dbsettings.database,
                                   host=dbsettings.host)
    cursor = conn.cursor()
    add_positionlog = ("INSERT INTO t (Date,T_max,T_min,mm,wind,wind_direction) VALUES (%(Date)s, %(T_max)s, %(T_min)s,%(mm)s,%(wind)s, %(wind_direction)s)")
    data_position = {
        'Date': date_yesterday,
        'T_max': max_temp,
        'T_min': min_temp,
        'mm': rain,
        'wind': Beaufort,
        'wind_direction': wind_direction,
    }

    cursor.execute(add_positionlog,data_position)
    conn.commit()
    cursor.close()
    conn.close()