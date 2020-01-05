import pandas as pd
import mysql.connector
import dbsettings

conn = mysql.connector.connect(user=dbsettings.user,
                                   password=dbsettings.password,
                                   database=dbsettings.database,
                                   host=dbsettings.host)


temps_prediction = pd.read_sql("""SELECT AVG((prediction.T_max - t.T_max)) AS T_max_error, AVG((prediction.T_min - t.T_min)) AS T_min_error, 
                                          prediction_in_days
                                          
                                  FROM prediction 
                                  INNER JOIN t on prediction.prediction_for = t.date 
                                  GROUP BY prediction_in_days""", conn)
