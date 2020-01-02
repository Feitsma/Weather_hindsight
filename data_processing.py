import mysql.connector
import dbsettings
from mysql.connector import Error
import numpy as np

#wat hersenspinsels om data uit sql te halen

try:
    connection = mysql.connector.connect(user=dbsettings.user,
                                         password=dbsettings.password,
                                         database=dbsettings.database,
                                         host=dbsettings.host)

    sql_select_Query = "select * from prediction"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in prediction is: ", cursor.rowcount)

    print("\nPrinting each prediction record")
    array = np.array([])
    for entry in records:
        print(entry)
        array = np.append(array, int(entry[7]))
        print('works')

except Error as e:
    print("Error reading data from MySQL table", e)

finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
