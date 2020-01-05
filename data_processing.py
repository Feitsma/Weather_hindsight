import mysql.connector
import dbsettings
from mysql.connector import Error
import numpy as np
import datetime
import matplotlib.pyplot as plt


try:
    connection = mysql.connector.connect(user=dbsettings.user,
                                         password=dbsettings.password,
                                         database=dbsettings.database,
                                         host=dbsettings.host)
    #import data from prediction database
    sql_select_Query = "select * from prediction"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    #import data from t database
    sql_select_Query_t = "select * from t"
    cursor_t = connection.cursor()
    cursor_t.execute(sql_select_Query_t)
    records_t = cursor_t.fetchall()


except Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


def max_temp_prediction():
    #This function creates an array of predicted max temperatures for the date of yesterday
    date_yesterday = records_t[-1][1]
    max_temps_14_days = []
    for entry in records:
        if entry[1] == date_yesterday:
            max_temps_14_days = np.append(max_temps_14_days, int(entry[2]))
    return max_temps_14_days

def min_temp_prediction():
    #This function creates an array of predicted max temperatures for the date of yesterday
    date_yesterday = records_t[-1][1]
    min_temps_14_days = []
    for entry in records:
        if entry[1] == date_yesterday:
            min_temps_14_days = np.append(min_temps_14_days, int(entry[3]))
    return min_temps_14_days

max_temps_14_days = max_temp_prediction()
min_temps_14_days = min_temp_prediction()

two_weeks = np.arange(start=1, stop=15, step=1)
plt.plot(two_weeks, max_temps_14_days, two_weeks, min_temps_14_days)