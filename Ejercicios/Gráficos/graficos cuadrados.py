'''
import matplotlib.pyplot as plt

cuadrados=[1,4,9,16,25]
fig, ax = plt.subplots()

ax.plot(cuadrados)

plt.show()
'''

#reto: Crear una list comprehension de los cuadrados de los 100 primeros números en lugar de introducirlos a mano.

import matplotlib.pyplot as plt
cuadrados= [n**2 for n in range(1,101)]
fig, ax = plt.subplots()

ax.plot(cuadrados)

plt.show()

# Informacion de la libreria: https://matplotlib.org/cheatsheets/
# Documentación: https://matplotlib.org/stable/index.html
# Tipos de gráficos: https://matplotlib.org/stable/plot_types/index.html
# Ejemplos: https://matplotlib.org/stable/gallery/index.html