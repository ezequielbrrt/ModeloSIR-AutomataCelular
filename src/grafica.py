#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modulo para graficar densidades de poblacion 
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(update):
    pullData = open("Datos/GraficaSano.txt","r").read()
    dataArray = pullData.split('\n')
    pullData2 = open("Datos/GraficaS.txt","r").read()
    dataArray2 = pullData2.split('\n')
    pullData3 = open("Datos/GraficaI.txt","r").read()
    dataArray3 = pullData3.split('\n')
    pullData4 = open("Datos/GraficaR.txt","r").read()
    dataArray4 = pullData4.split('\n')
    xar = []
    yar = []
    xar2 = []
    yar2 = []
    xar3 = []
    yar3 = []
    xar4 = []
    yar4 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            y,x = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    for eachLine2 in dataArray2:
    	if len(eachLine2)>1:
            y2,x2 = eachLine2.split(',')
            xar2.append(int(x2))
            yar2.append(int(y2))
    for eachLine3 in dataArray3:
    	if len(eachLine3)>1:
            y3,x3 = eachLine3.split(',')
            xar3.append(int(x3))
            yar3.append(int(y3))
    for eachLine4 in dataArray4:
    	if len(eachLine4)>1:
            y4,x4 = eachLine4.split(',')
            xar4.append(int(x4))
            yar4.append(int(y4))                
    ax1.clear()
    ax1.plot(xar,yar,color="yellow",linestyle="-", label="Sano",linewidth=2.5)
    ax1.plot(xar2,yar2,color="green",linestyle="-", label="Suceptible",linewidth=2)
    ax1.plot(xar3,yar3,color="red",linestyle="-", label="Infectado",linewidth=2)
    ax1.plot(xar4,yar4,color="blue",linestyle="-", label="Recuperado",linewidth=2.5)
    plt.legend(loc='upper left', frameon=False)
    #ax1.bar(xar,yar, facecolor='#9999ff',label="Poblacion")
    plt.title("Poblacion")
    plt.xlabel("Tiempo ")
    plt.ylabel("Personas")
    plt.grid(True)

ani = animation.FuncAnimation(fig , animate, interval=1000)
plt.show()
