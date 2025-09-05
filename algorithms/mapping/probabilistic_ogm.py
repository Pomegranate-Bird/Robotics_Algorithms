import numpy as np
import random

GRID_Height = 10
GRID_WIDTH  = 10
INIT_UNCERTAINTY = 0.5 
OCCUPIED = 1 
UNOCCUPIED = 0

#Intializing an Occupancy Grid map 
grid = np.zeros((GRID_Height,GRID_WIDTH)) 


#Assigning all cells an intial uncertainty to the Occuopancy Grid Map 
grid[:, :] = INIT_UNCERTAINTY

# Creating a wall within the map(occupied cells)
wall = grid[3:, 3] = OCCUPIED
staticmethod = wall # Static object within the envioremnt 

# Scattering random objects throughout the map
deafult_rng = np.random.default_rng()

random_probabilities = deafult_rng.random()

# Appending some of the random values to a section of the array 

objects = grid[:, :] = random_probabilities

staticmethod = objects # Making the objects static for now

print(grid)