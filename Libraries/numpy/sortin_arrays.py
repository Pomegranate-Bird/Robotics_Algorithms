import numpy as np

eye = np.eye(3) #the rows are 0,1,2

eye[2:, 2] = 5 # assigning index row 2 column 2 value 5

sortedeye = np.sort(eye) # sorts indexes by least to greatest by row so small smal big for one row and then the next

#sorting by rows
sortedeye = np.sort(eye, axis = 0) # -1 is rows and 0 is columns, now sorting by columns 

print(sortedeye)