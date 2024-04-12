import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)

    # Obten las fechas y las temperaturas mininimas del fichero.
    fechas, maximas, mininimas = [], [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        min = int(fila[6])
        mininimas.append(min)
        max= int(fila[5])
        maximas.append(max)


# Dibuja las temperaturas mininimas.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, mininimas, c='cian')
ax.plot(fechas, maximas, c='red')

# Formatea el gráfico.
plt.title("Temperaturas diarias mínimas - 2018", fontsize=24)
plt.xlabel('Fechas', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.fill_between(fechas, maximas, min, facecolor= 'blue', alpha='red')