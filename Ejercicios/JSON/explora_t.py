import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explora la estuctura de datos.
nombreFichero = 'datos/eq_data_30_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes, titulo, textos_hover = [], [], [], [], []
for diccTerremotos in todos_los_diccionarios:
    magnitud= diccTerremotos['properties']['mag']
    longitud= diccTerremotos['geometry']['coordinates'][0]
    latitud= diccTerremotos['geometry']['coordinates'][1]
    titulo= diccTerremotos['properties']['title']
    magnitudes.append(magnitud)
    longitudes.append(longitud)
    latitudes.append(latitud)
    textos_hover.append(titulo)

#Ubica los terremotos en el mapa
data= [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': textos_hover,
    'marker':{
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitud'},
    },
}]

mi_disposicion = Layout(title= 'Terremotos Globales')
fig = {'data': data, 'layout': mi_disposicion}
offline.plot(fig, filename= 'terremotos_globales.html')