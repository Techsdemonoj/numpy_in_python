# Slicing array - slicing in python means taking elemenys from one given index to another index.
# [start_index:end_index], [start_index:end_index:step_index]

# Now we will slice an element from 1 to 5 :
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
# heren we slicing basis on index and index start with 0th
print(array1[1:5])              #____________________________________________ [start_index:end_index]
# result = [2 3 4 5]


# now we will slice from index 4 to the end value
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[4:])               #_____________________________________________________ [start_index:        ]
# result = [ 5  6  7  8  9 10]

# now we will slice from the begining ndex 4
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[:4])                #_________________________________________________ [           :end_index]
# result = [1 2 3 4]


# Negetive Slicing - index 3 to end
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[-6:-1]) 
# result = [5 6 7 8 9]
print(array1[-3:-1])
# result = [8 9]


# Steps: you will use step value to detemine the step of the slicing
# return every other value fromcindex 1 to 5
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[1:5:2])            #_________________________________________ [start_index:end_index:step_index]
# result = [2 4]


# now return every other number from the entire array
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[::2])              #_________________________________________ [        :       :step_index] 
# result = [1 3 5 7 9]


# Slicing 2-D array
import numpy as np
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1:4])
# result = [7 8 9]


# Another example 
import numpy as np
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[0:2, 2])
# result = [3 8]


# Another example 
import numpy as np
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[0:2, 1:4])
# result = [3 8]





