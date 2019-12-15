import mysql.connector
import dbsettings



def add(table,day,T_max,T_min,prec_prob,mm,wind,prediction_in_days):
    conn = mysql.connector.connect(user=dbsettings.user, password=dbsettings.password, database=dbsettings.database,
                                   host=dbsettings.host)
    cursor = conn.cursor()
    add_positionlog = ("INSERT INTO " + table + " (DateTime,T_max,T_min,prec_prob,mm,wind,prediction_in_days) VALUES (%(DateTime)s, %(T_max)s, %(T_min)s, %(prec_prob)s,%(mm)s,%(wind)s,%(prediction_in_days)s)")
    data_position = {
    'DateTime': day,
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
