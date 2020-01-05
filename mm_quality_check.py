import pandas as pd
import mysql.connector
import dbsettings

conn = mysql.connector.connect(user=dbsettings.user,
                               password=dbsettings.password,
                               database=dbsettings.database,
                               host=dbsettings.host)

temps_prediction = pd.read_sql("""SELECT 
                                    AVG((ABS(prediction.mm - t.mm))) AS mm_error, 
                                    prediction_in_days

                                  FROM prediction 
                                  INNER JOIN t on prediction.prediction_for = t.date 
                                  GROUP BY prediction_in_days""", conn)

temps_prediction.plot(x='prediction_in_days', y='mm_error')

