# Difference between numpy array copy and view.
# we will make a copy, change original array and display both.
import numpy as np
array1 = np.array([1,2,3,4,5])
array2 = array1.copy()
array2[0]= 12
print(array1)
print(array2)

# now we will make a view, change original,display both


import numpy as np
array1 = np.array([1,2,3,4,5])
array2 = array1.view()
array1[0] = 42
print(array1)
print(array2)





















