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
import time
import generacion

#variables
tiempo = 0
var = 0
border = 0
alsk = 0
auxestados = []
contador = -1
pasada = 1
sano,s,inf,r= 0,0,0,0

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
pullData = open("Datos/Poblacion.txt","r").read()
dataArray = pullData.split('\n')
datos = open("Datos/Estados.txt","r").read()
estados = datos.split('\n')
estados = filter(None, estados)#dibujando los estados deacuerdo a su valor

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
grafica = open("Datos/GraficaSano.txt","w")
grafica.close()
grafica = open("Datos/GraficaS.txt","w")
grafica.close()
grafica = open("Datos/GraficaI.txt","w")
grafica.close()
grafica = open("Datos/GraficaR.txt","w")
grafica.close()

#metodo de escribirConteo
def escribirConteo(auxestados):
    global sano,s,inf,r
    for it in auxestados:
        if it == "0":
            sano += 1
        if it == "1":
            s += 1
        if it == "2":
            inf += 1
        if it == "3":
            r += 1
    grafica = open("Datos/GraficaSano.txt","a")
    grafica.write(str(sano)+","+str(tiempo)+"\n")
    grafica = open("Datos/GraficaS.txt","a")
    grafica.write(str(s)+","+str(tiempo)+"\n")
    grafica = open("Datos/GraficaI.txt","a")
    grafica.write(str(inf)+","+str(tiempo)+"\n")
    grafica = open("Datos/GraficaR.txt","a")
    grafica.write(str(r)+","+str(tiempo)+"\n")

def conteo(auxestados):
    global sano,s,inf,r
    for it in auxestados:
        if it == "0":
            sano += 1
        if it == "1":
            s += 1
        if it == "2":
            inf += 1
        if it == "3":
            r += 1
   

#funcion para poner colores a los estados
def set_color(auxestados):
    border = 0
    var = 0
    global xar,yar
    for valor in auxestados:  
        border = border + 1
        if border < len(auxestados):        
            if valor == "0":
                map.plot(xar[var],yar[var], "yo")
            if valor == "1":
                map.plot(xar[var],yar[var], "go")
            if valor == "2":
                map.plot(xar[var],yar[var], "ro")
            if valor == "3":
                map.plot(xar[var],yar[var], "bo")
            var = var + 1

# funcion de animacion
def animate(i):
    global estados
    global lat,lon
    global auxestados
    global pasada, var, border,tiempo
    global sano,s,inf,r
    if pasada > 1:
        auxestados = estados
        conteo(auxestados)
        for x in range(len(estados)):
            if pasada :
                total = sano + s + inf + r
                psano = (sano * 100)/float(total)
                ps = (s * 100)/float(total)
                pinf = (inf * 100)/float(total)
                pr = (r * 100)/float(total)
                
                seleccion = np.random.choice(2,1,p=[0.6,0.4])
                if seleccion[0] == 0:
                    distribucion = np.random.choice(2,1,p=[0.5,0.5])
                    if distribucion[0] == 1 and auxestados[x] == "2":
                        auxestados [x] = "3"
                if seleccion[0] == 1:
                    distribucion2 = np.random.choice(2,1,p=[0.5,0.5])
                    if distribucion2[0] == 1 and auxestados[x] == "1" :
                        auxestados[x] = "0"
                    elif distribucion2[0] == 0 and auxestados[x] == "1":
                        auxestados[x] = "2"
                    #auxestados[x] = "3"
                #auxestados.append(str(estados[x]))
            else:
                pass
                #auxestados.append(str(estados[x]))
        total, psano,ps,pinf,pr = 0,0,0,0,0 
        escribirConteo(auxestados)
        set_color(auxestados)
        sano,s,inf,r = 0,0,0,0
    if pasada == 1 :
        set_color(estados)
        escribirConteo(estados)
        sano,s,inf,r = 0,0,0,0
    tiempo += 1
    pasada += 1
    auxestados = []
    return alsk,

#time.sleep(10)
anim = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.title("SIMULACION DE LA PROPAGACION DEL DENGUE")
plt.show()
