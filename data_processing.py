import mysql.connector
import dbsettings
from mysql.connector import Error
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.pyplot as point



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

def yesterdays_temps():
    #This function gets temps of yesterday
    T_max_yesterday = records_t[-1][2]
    T_min_yesterday = records_t[-1][3]
    return T_max_yesterday, T_min_yesterday

def yesterday_rain():
    #get mm of rain yesterday
    mm_yesterday = records_t[-1][4]
    return mm_yesterday

def rain_prediction():
    #create and array of predicted amount of rain of yesterday
    date_yesterday = records_t[-1][1]
    mm_14_days = []
    for entry in records:
        if entry[1] == date_yesterday:
            mm_14_days = np.append(mm_14_days, float(entry[4]))
    return mm_14_days

def plot_temp_outlook():
    #create 14 day plot with temperature outlook for day of yesterday
    max_temps_14_days = max_temp_prediction()
    min_temps_14_days = min_temp_prediction()
    temps_yesterday = yesterdays_temps()
    T_max_yesterday = temps_yesterday[0]
    T_min_yesterday = temps_yesterday[1]
    date_yesterday = records_t[-1][1]
    two_weeks = np.arange(start=-14, stop=0, step=1)
    max_temp_pred_plot = plt.plot(two_weeks, max_temps_14_days, '.C1-', label='max. temp. prediction')
    min_temp_pred_plot = plt.plot(two_weeks, min_temps_14_days, '.C0-', label='min. temp. prediction')
    act_max_temp_plot = plt.plot(0,T_max_yesterday,'ro', label='Actual max. T')
    act_min_temp_plot = plt.plot(0,T_min_yesterday,'b*', label='Actual min. T')
    plt.legend()
    plt.title('Temperature Outlook for ' + str(date_yesterday))
    plt.xlabel('Outlook in days')
    plt.ylabel('Temperature ($^\circ$C)')
    return plt

def plot_rain_outlook():
    #create 14 day plot with amount of rain outlook for day of yesterday
    mm_yesterday = yesterday_rain()
    mm_14_days = rain_prediction()
    date_yesterday = records_t[-1][1]
    two_weeks = np.arange(start=-14, stop=0, step=1)
    mm_pred_plot = plt.plot(two_weeks, mm_14_days, '.C1-', label='precipitation outlook')
    act_mm_plot = plt.plot(0,mm_yesterday,'ro', label='Actual precipitation')
    plt.legend()
    plt.title('Precipitation Outlook for ' + str(date_yesterday))
    plt.xlabel('Outlook in days')
    plt.ylabel('Precipitation (mm)')
    return plt

#plot_temp_outlook()
plot_rain_outlook()
print(yesterday_rain())
print(rain_prediction())