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
lat = []
lon = []
# funcion de animacion
def animate(i):
    """
    lons  =  np.random.uniform(-97, -85, 1)
    lats = np.random.uniform(14.5, 21, 1)
    if lats[0] < 23 and lons[0] < -106:
        return
    if lats[0] < 16 and lons[0] < -93:
        return
    if lats[0] > 23 and lons[0] < -110:
        return
    if lats[0] < 29 and lats[0] > 21: 
        if lons[0] > -97:
            return
    """
    for eachLine in dataArray:
        if len(eachLine)>1:
            x ,y = eachLine.split(',')
            lat.append(float(x))
            lon.append(float(y))
        xar, yar = map(lon,lat)
        point = map.plot(xar,yar, 'ro')
    
    #obtener una mejor distribucion
    #s = np.random.uniform(1,0,2)
    #print s
    
    return point,


#fig = plt.subplot()
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, interval=1)
plt.title("SIMULACION DE LA PROPAGACION DEL DENGUE")
plt.show()
