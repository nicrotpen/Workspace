import csv

nombreFichero = 'datos/sitka_weather_2018_simple.csv'
with open(nombreFichero) as f:
    lector = csv.reader(f)
    fila_cabecera = next(lector)
    #print(fila_cabecera)
    temperaturas_maximas=[]
    for fila in lector:
        max=int(fila[5])
        temperaturas_maximas.append(max)

import matplotlib.pyplot as plt

ej_y=temperaturas_maximas
plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
ax.plot(ej_y, c='pink')
ax.set_title("Temperaturas Máximas", fontsize=18)
ax.set_ylabel("Temperaturas (ºF)", fontsize=12)
ax.set_xlabel("Medidas", fontsize=12)

plt.show()

