#!/usr/bin/env python
 # -*- coding: utf-8 -*-
"""
Archivo mapa.py que sirve para dibujar el mapa 
de méxico 
"""


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from pylab import *
import numpy as np

#configuación del los valores del mapa
map = Basemap(projection='mill',llcrnrlat=14.5,urcrnrlat=33,\
                llcrnrlon=-120,urcrnrlon=-85,resolution='c')
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='#7F5454',lake_color= "#6F9CF5")
map.drawmapboundary(fill_color= "#6F9CF5")
map.drawstates()

#se asigna un nuevo tamaño a la ventana del mapa
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5, forward = True)

#recoleccion de datos 
pullData = open("Poblacion.txt","r").read()
dataArray = pullData.split('\n')
datos = open("Estados.txt","r").read()
estados = datos.split('\n')

#generacion de coordenadas
lat = []
lon = []
for eachLine in dataArray:
    if len(eachLine)>1:
        x ,y = eachLine.split(',')
        lat.append(float(x))
        lon.append(float(y))    
xar, yar = map(lon,lat)

#generacion de graficas de densidades de estadisticas
"""
sano = 0
s = 0
inm = 0
r = 0
for i in estados:
    if i == ""0"":
        sano += 1
    if i == "1":
        s += 1
    if i == "2":
        inm += 1
    if i == "3":
        r += 1
"""


#dibujando los estados deacuerdo a su valor
var = 0
border = 0
for valor in estados:  
    border = border + 1
    if border < len(estados):        
        if valor == "0":
            point = map.plot(xar[var],yar[var], "yo")
        if valor == "1":
            point = map.plot(xar[var],yar[var], "go")
        if valor == "2":
            point = map.plot(xar[var],yar[var], "bo")
        if valor == "3":
            point = map.plot(xar[var],yar[var], "ro")
        var = var + 1

#creacion de estadisticas de estados


# funcion de animacion

def animate(i):
    
    return point,


#anim = animation.FuncAnimation(plt.gcf(), animate, interval=1)
plt.title("SIMULACION DE LA PROPAGACION DEL DENGUE")
plt.show()
