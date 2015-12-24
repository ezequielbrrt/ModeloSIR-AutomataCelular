#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
ON = 1
OFF = 0
vals = [ON, OFF]

grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)


def update(data):
  global grid
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
      if grid[i, j]  == ON:
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]
  
fig, ax = plt.subplots()
mat = ax.matshow(grid,cmap=plt.get_cmap('hot'), interpolation='nearest',
               vmin=0, vmax=1)
ani = animation.FuncAnimation(fig, update, interval=1,)
plt.show()


"""

from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

datos = open("Poblacion.txt","w")
datos.close()

for x in range(1,10000):
	longitud = np.random.uniform(-97,-85,1)
	latitud = np.random.uniform(14.5,21,1)

	if latitud[0] < 16 and longitud[0] < -93:
	    pass
	if latitud[0] < 20 and longitud[0] < -87:
		pass
	else:
		datos = open("Poblacion.txt","a")	
		datos.write(str(latitud[0])+","
			+str(longitud[0])+"\n")
		datos.close()
	