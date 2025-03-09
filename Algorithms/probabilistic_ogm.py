import numpy as np
from numpy.random import default_rng

GRID_Height = 100
GRID_WIDTH  = 100
INIT_UNCERTAINTY = 0.5 

#Intializing an Occupancy Grid map 
grid = np.zeros((GRID_Height,GRID_WIDTH)) 


#Assigning some probabilities to the Occuopancy Grid Map 

grid[:, :] = 0.5

print(grid)