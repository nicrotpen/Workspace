import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero1 = 'datos/sitka_weather_2018_simple.csv'
nombreFichero2 = 'datos/death_valley_2018_simple.csv'

with open(nombreFichero1) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas mininimas del fichero.
    fechas, maximas1, minimas1 = [], [], []
    for fila in lector:

        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        min1 = int(fila[6])
        minimas1.append(min1)
        max1= int(fila[5])
        maximas1.append(max1)

with open(nombreFichero2) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas mininimas del fichero.
    maximas2, minimas2 = [], []
    for fila in lector:
    
        min2 = int(fila[5])
        minimas2.append(min2)
        max2= int(fila[4])
        maximas2.append(max2)


# Dibuja las temperaturas mininimas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, minimas1, c='blue')
ax.plot(fechas, maximas1, c='red')
ax.plot(fechas, minimas2, c='blue')
ax.plot(fechas, maximas2, c='red')

# Formatea el gráfico.
plt.title("Temperaturas Sitka-Death Valley 2018", fontsize=24)
plt.xlabel('Fechas', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperaturas (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.fill_between(fechas, maximas1, minimas1, facecolor= 'blue', alpha=0.1)
plt.fill_between(fechas, maximas2, minimas2, facecolor= 'blue', alpha=0.1)
plt.show()