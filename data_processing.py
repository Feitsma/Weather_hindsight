import mysql.connector
import dbsettings
from mysql.connector import Error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    connection = mysql.connector.connect(user=dbsettings.user,
                                         password=dbsettings.password,
                                         database=dbsettings.database,
                                         host=dbsettings.host)
    #import all (*) data from database 'prediction'
    sql_select_Query = "select * from prediction"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    #import all (*) data from table 't'
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
    date_yesterday = records_t[-1][1] #get most recent entry (row), column 1
    max_temps_14_days = []
    for entry in records:
        if entry[1] == date_yesterday: #if a row contains the date of yesterday, get value from column 2, which is maxT.
            max_temps_14_days = np.append(max_temps_14_days, int(entry[2]))
    return max_temps_14_days

def min_temp_prediction():
    #This function creates an array of predicted max temperatures for the date of yesterday
    date_yesterday = records_t[-1][1] #get most recent entry (row), column 1
    min_temps_14_days = []
    for entry in records:
        if entry[1] == date_yesterday: #if a row contains the date of yesterday, get value from column 2, which is maxT.
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

def yesterday_wind():
    #get wind force of yesterday
    wind_yesterday = records_t[-1][5]
    return wind_yesterday

def rain_prediction():
    #create and array of predicted amount of rain of yesterday
    date_yesterday = records_t[-1][1]
    mm_14_days = []
    for entry in records:
        if entry[1] == date_yesterday:
            mm_14_days = np.append(mm_14_days, float(entry[5]))
    return mm_14_days

def wind_prediction():
    #create and array of predicted amount of wind of yesterday
    date_yesterday = records_t[-1][1]
    wind_14_days = []
    for entry in records:
        if entry[1] == date_yesterday:
            wind_14_days = np.append(wind_14_days, int(entry[6]))
    return wind_14_days

def plot_temp_outlook():
    #create 14 day plot with temperature outlook for day of yesterday
    max_temps_14_days = max_temp_prediction()
    min_temps_14_days = min_temp_prediction()
    temps_yesterday = yesterdays_temps()
    T_max_yesterday = temps_yesterday[0]
    T_min_yesterday = temps_yesterday[1]
    date_yesterday = records_t[-1][1]
    two_weeks = np.arange(start=-14, stop=0, step=1) #initiate x axis as time, from -14 to 0 (yesterday)
    max_temp_pred_plot = plt.plot(two_weeks, max_temps_14_days, '.C1-', label='max. temp. prediction')
    min_temp_pred_plot = plt.plot(two_weeks, min_temps_14_days, '.C0-', label='min. temp. prediction')
    act_max_temp_plot = plt.plot(0,T_max_yesterday,'ro', label='Actual max. T')
    act_min_temp_plot = plt.plot(0,T_min_yesterday,'b*', label='Actual min. T')

    #plt.ioff() # Disable showing of plots
    plt.legend()
    plt.title('Temperature Outlook for ' + str(date_yesterday)) #add title with date as variable in name
    plt.xlabel('Outlook in days')
    plt.ylabel('Temperature ($^\circ$C)')
    plt.savefig('/var/www/hp-iot/images/weather-hindsight/temp_outlook.png') #save img on webpage-callable location
    plt.close()
    return plt #return the plot

def plot_rain_outlook():
    #create 14 day plot with amount of rain outlook for day of yesterday
    mm_yesterday = yesterday_rain()
    mm_14_days = rain_prediction()
    date_yesterday = records_t[-1][1]
    two_weeks = np.arange(start=-14, stop=0, step=1)
    mm_pred_plot = plt.plot(two_weeks, mm_14_days, '.C1-', label='precipitation outlook')
    act_mm_plot = plt.plot(0,mm_yesterday,'ro', label='Actual precipitation')

    #plt.ioff()  # Disable showing of plots
    plt.legend()
    plt.title('Precipitation Outlook for ' + str(date_yesterday)) #add title with date as variable in name
    plt.xlabel('Outlook in days')
    plt.ylabel('Precipitation (mm)')
    plt.savefig('/var/www/hp-iot/images/weather-hindsight/rain_outlook.png')
    plt.close()
    return plt

def plot_wind_outlook():
    #create 14 day plot with wind force outlook for day of yesterday
    wind_14_days = wind_prediction()
    date_yesterday = records_t[-1][1]
    two_weeks = np.arange(start=-14, stop=0, step=1)
    wind_yesterday = yesterday_wind()
    wind_pred_plot = plt.plot(two_weeks, wind_14_days, '.C0-', label='wind force prediction')
    act_wind_plot = plt.plot(0,wind_yesterday,'bo', label='Actual wind')

    #plt.ioff() # Disable showing of plots
    plt.legend()
    plt.title('Wind force Outlook for ' + str(date_yesterday))
    plt.xlabel('Outlook in days')
    plt.ylabel('Wind (Beaufort)')
    plt.savefig('/var/www/hp-iot/images/weather-hindsight/wind_outlook.png')
    plt.close()
    return plt


def plot_average_temp_error():
    """Plots the average total error vs days of prediction, and saves the plot on webserver"""

    conn = mysql.connector.connect(user=dbsettings.user,
                                   password=dbsettings.password,
                                   database=dbsettings.database,
                                   host=dbsettings.host)

    temps_prediction = pd.read_sql("""SELECT 
                                        AVG((ABS(prediction.T_max - t.T_max))) AS T_max_error, 
                                        AVG((ABS(prediction.T_min - t.T_min))) AS T_min_error, 
                                        (prediction_in_days * -1) AS prediction_in_days
    
                                      FROM prediction 
                                      INNER JOIN t on prediction.prediction_for = t.date 
                                      GROUP BY prediction_in_days""", conn)

    plt.ioff()
    plot = temps_prediction.plot(x='prediction_in_days', y=['T_max_error', 'T_min_error'],
                                 title='Average error in temperature outlook')
    plot.set_xlabel('Outlook in days')
    plot.set_ylabel('Temperature ($^\circ$C)')
    plot = plot.get_figure()
    # Save figure to webserver location
    plot.savefig('/var/www/hp-iot/images/weather-hindsight/temp_average_outlook.png')


def plot_average_mm_error():
    """Plots the average total error vs days of prediction, and saves the plot on webserver"""

    conn = mysql.connector.connect(user=dbsettings.user,
                                   password=dbsettings.password,
                                   database=dbsettings.database,
                                   host=dbsettings.host)

    temps_prediction = pd.read_sql("""SELECT 
                                        AVG((ABS(prediction.mm - t.mm))) AS mm_error, 
                                        (prediction_in_days * -1) AS prediction_in_days
    
                                      FROM prediction 
                                      INNER JOIN t on prediction.prediction_for = t.date 
                                      GROUP BY prediction_in_days""", conn)

    plt.ioff()
    plot = temps_prediction.plot(x='prediction_in_days', y='mm_error', title='Average error in precipitation outlook')
    plot.set_xlabel('Outlook in days')
    plot.set_ylabel('Precipitation (mm)')
    plot = plot.get_figure()
    #Save figure to webserver location
    plot.savefig('/var/www/hp-iot/images/weather-hindsight/rain_average_outlook.png')




plot_temp_outlook()
plot_rain_outlook()
plot_wind_outlook()
plot_average_temp_error()
plot_average_mm_error()
