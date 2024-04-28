# Shape of an array- the shape of an array is the number of elements in each direction.
# Now we will try to get the shape of an array
import numpy as np
array1 = np.array([[1,2,3,4],[5,6,7,8]])
print(array1.shape) # (2,4)
# which means the array has 2 dimensions and it has 4 elements

# Now we will create 5-D dimentions array using ndim :
import numpy as np
array2 = np.array([41,42,43,44],ndmin=5 )
print(array2)
print('shape of array is',array2.shape)
















