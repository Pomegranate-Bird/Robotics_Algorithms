import numpy as np

array = np.eye(3)
myview = array.view()  # can change the original array
my_copy = array.copy() # is a copy of the array another object 

myview [:] = 3
print(myview)

print(array) # The original array was changed (shape wont' change but values of the array will)


