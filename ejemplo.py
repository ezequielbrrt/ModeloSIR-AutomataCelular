from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 10
ON = 1
OFF = 0
vals = [ON, OFF]

grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
gridf = np.random.random_sample((5,10))

print grid
print
print gridf