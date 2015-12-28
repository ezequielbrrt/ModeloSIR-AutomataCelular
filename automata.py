#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


#Creacion de la Poblacion
datos = open("Poblacion.txt","w")
datos.close()

datos = open("Estados.txt","w")
datos.close()

estado = 1
contador = 0

for x in range(1,200):
	longitud = np.random.uniform(-108,-85,1)
	latitud = np.random.uniform(14.5,25,1)
	lon = longitud[0]
	lat = latitud[0]
	#poniendo limites
	if lat < 16 and lon < -93:
		pass
	elif lat < 25 and lat > 19 and lon < -91 and lon > -97 : 
		pass
	elif lon > -88 and lat > 16:
		pass
	elif lat > 21 and lon > -91:
		pass
	elif lat < 23.5 and lon < -106:
		pass 
	elif lat < 18 and lon < -101:
		pass
	elif lat > 22 and lon > -98:
		pass
	elif lat < 24.39 and lon < -107:
		pass
	elif lat < 20.4 and lon < -105.5:
		pass
	else:
		contador = contador + 1
		datos = open("Poblacion.txt","a")	
		datos.write(str(lat)+","
			+str(lon)+"\n")
		datos.close()


v = np.random.choice(4, contador, p=[0.3, 0.2, 0.3, 0.2])
for i in v:
	data = open("Estados.txt","a")
	data.write(str(i)+"\n")
	data.close()
	