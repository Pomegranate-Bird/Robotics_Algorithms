import numpy as np
import pybullet as p
import time
import pybullet_data

#Graphical Interface Slected
physics_client = p.connect(p.GUI)

#Setting additional seach paths for accessing URDF' easily 
addittional_search_paths = p.setAdditionalSearchPath(pybullet_data.getDataPath()) # Optional but really useful so not really optional 

#Gravity for the simulation 
Gravity = p.setGravity(0,0,-9.8) 

plane_id = p.loadURDF("plane.urdf")

plane_init_pos = [0,0,0] # Assigning a starting position to the plane 

plane_orientation = p.getQaternionFromEuler([0,0,0]) #plane orientation

robot_init_orientation = p.getQaternionFromEuler([0,0,0]) # RObot orientation
robot_init_pos = [0,0,0]

#Loading in R2D2 Robot into the plane 
robot = p.loadURDF("r2d2.urdf", robot_init_pos ,robot_init_orientation)

while(True):
    p.stepSimulation()
    time.sleep(1/240)
    ...




