#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archivo mapa.py que sirve para dibujar el mapa 
de méxico 
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *
import numpy as np

def update(data):


    """
    COMO GRAFICAR PUNTOS

    # Houston, Texas

    lat,lon = 29.7630556,-95.3630556
    x,y = m(lon,lat)
    m.plot(x,y, 'ro')
    

    lon, lat = -104.237, 40.125 # Location of Boulder

    xpt,ypt = m(lon,lat)
    m.plot(xpt,ypt, 'go')
    """
    #canbia el tamaño de la ventana
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5, forward = True)
 

m = Basemap(projection='mill',llcrnrlat=14.5,urcrnrlat=33,\
                llcrnrlon=-120,urcrnrlon=-85,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')

ani = animation.FuncAnimation(m,update,interval=1)
plt.title("PROPAGACION DEL DENGUE EN MEXICO")
plt.show()
