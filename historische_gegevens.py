import pandas as pd
import numpy as np





#Makkelijk te scrapen
weerstatistieken = pd.read_html('https://weerstatistieken.nl/eelde/2019/december')
temperaturen = weerstatistieken[0] #pak de tabel met temperatuurdata
vandaag = temperaturen.iloc[13] #vandaag is het de 14e, maar 13 ivm python indexing
max = vandaag[2] #max temperatuur vandaag
min = vandaag [1]
