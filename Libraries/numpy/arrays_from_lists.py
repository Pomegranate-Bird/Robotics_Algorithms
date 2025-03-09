import numpy as np 

# from_list = np.array([1,2,3], dtype = np.int8) # To avoid using 64 bits by using 8 bits instead
# print(type(from_list[0]))


#2D arrays 
# two_bytwo = np.array(([1,2,3],[1,2,3]), dtype = np.int8)
# print(two_bytwo)

#We can also make arrays with the arrange function 
#ogm = np.array((np.arange(0,1,0.01), np.arange(0,1,0.01)))
# print(ogm)
#print(ogm.shape) # Returns (2,100) a 2x100 matrix 

# What if we do not want it to be a 2x100 matrix, we can reshape it 
#ogm = ogm.reshape((2,100))
#print(ogm)

#Creating an empty array
# empty_grid = np.zeros((2,2))
# empty_grid = np.ones((2,2))
# print(empty_grid)

# Creating an identity matrix, we're not restricted to the main diagonal 
eye_array = np.eye(3)
#print(eye_array)

#Example
eye_array = np.eye(3, k = 1) # choosing the daigonal above main 
eye_array[eye_array ==0] = 2 # Set all values of 0 within the eyearray equal to 2
eye_array[eye_array < 2] = 9 # Set all the values within the eyearray that are less than 2 as 9
eye_array[:2] = 3 # Selecting the two rows and setting the values to 3 
eye_array[1:] = 10 # Selecting all rows past row 0 and setting the values to 10
eye_array[:,0] = 4 #selecting all the rows and selecting column 0 and setting all of it's values to 4
eye_array[2:, 0] = 90
print(eye_array)



