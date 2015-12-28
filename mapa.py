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

lat = []
lon = []
est = []
for eachLine in dataArray:
    if len(eachLine)>1:
        x ,y = eachLine.split(',')
        lat.append(float(x))
        lon.append(float(y))
    
xar, yar = map(lon,lat)
#colores bo = azul, ro = rojo, go=verde, yo = amarillo
border = 0
for each in estados:
    border = border + 1
    if border < len(estados):
        est.append(int(each))

#dibujando los estados deacuerdo a su valor
var = 0
border = 0
for valor in est:  
    border = border + 1
    if border < len(est):        
        if valor == 0:
            point = map.plot(xar[var],yar[var], "yo")
        if valor == 1:
            point = map.plot(xar[var],yar[var], "go")
        if valor == 2:
            point = map.plot(xar[var],yar[var], "bo")
        if valor == 3:
            point = map.plot(xar[var],yar[var], "ro")
        var = var + 1


# funcion de animacion

def animate(i):
    
    return point,


#anim = animation.FuncAnimation(plt.gcf(), animate, interval=1)
plt.title("SIMULACION DE LA PROPAGACION DEL DENGUE")
plt.show()
