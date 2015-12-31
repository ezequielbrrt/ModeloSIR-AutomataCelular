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

#generacion de coordenadas 
contador = 0
for x in range(1,20000):
	longitud = np.random.uniform(-108,-85,1)
	latitud = np.random.uniform(14.5,25,1)
	lon = longitud[0]
	lat = latitud[0]
	#poniendo limites
	if lat < 16.3 and lon < -92.38:
		pass
	elif lat < 25 and lat > 18.119 and lon < -90.4 and lon > -97 : 
		pass
	elif lon > -88 and lat > 16:
		pass
	elif lat > 24 and lon > -91:
		pass
	elif lat < 23.7 and lon < -105.5:
		pass 
	elif lat < 18.27 and lon < -101:
		pass
	elif lat > 20.6 and lon > -98:
		pass
	elif lat < 24.39 and lon < -106.7:
		pass
	elif lat < 20.4 and lon < -105.3:
		pass
	elif lat < 18 and lon > -91:
		pass
	elif lat < 17.399  and lon < -98:
		pass
	elif lat < 19.7 and lon < -103.6:
		pass
	else:
		contador = contador + 1
		datos = open("Poblacion.txt","a")	
		datos.write(str(lat)+","
			+str(lon)+"\n")
		datos.close()


#generacion de estados
sano = 0.3
s = 0.2
inm = 0.3
r = 0.2
v = np.random.choice(4, contador, p=[sano, s, inm, r])
for i in v:
	data = open("Estados.txt","a")
	data.write(str(i)+"\n")
	data.close()		