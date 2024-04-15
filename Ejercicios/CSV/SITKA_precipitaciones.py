import csv
from datetime import datetime

from matplotlib import pyplot as plt

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
nombre_estacion=''
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)
    leido=0
    # Obten las fechas y las temperaturas precipitacions del fichero.
    fechas, precipitaciones = [], []
    for fila in lector:
        fecha_actual = datetime.strptime(fila[2], '%Y-%m-%d')
        fechas.append(fecha_actual)
        precipitacion = float(fila[3])
        precipitaciones.append(precipitacion)
        if not(leido):
            nombre_estacion=fila[1]
            leido=1

# Dibuja las temperaturas precipitacions.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(fechas, precipitaciones, c='red')


# Formatea el gráfico.
plt.title(f"Precipitaciones diarias \n - 2018 en {nombre_estacion}", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatura (ºF)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

