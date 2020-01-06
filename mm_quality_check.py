import pandas as pd
import mysql.connector
import dbsettings
import matplotlib.pyplot as plt

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
plot.savefig('/var/www/hp-iot/images/weather-hindsight/rain_average_outlook.png')

