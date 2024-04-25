# how  we will create a numpy ndarray object
# the array object in numpy is call ndarray.
# array()

import numpy as np
x = np.array([1,2,3,4,5])
print(x) 
print(type(x))              # output = [1 2 3 4 5]

# we can also pass a list, tuple or any array like object with array().
# it will be converted to ndarray
import numpy as np
y =np.array((1,2,3,4,5))

print(x)
print(type(x))               # output = [1 2 3 4 5]

# Dimension in array: a dimension is arrays is one level of array depth(nested array)

# O-D Arrays - scalars, are the elements in an array, each value in an array is O-D Arrays.

# Now we will create  O-D arrays with value 42
import numpy as np
x = np.array(42)
print(x)                    # output = 42


# 1-D Arrays: an arrays that has 0-D Arrays as its elements is called uni dimentional OR 1-D
import numpy as np
array1 =np.array([1,2,3,4,5])
print(array1)                   # output = [1 2 3 4 5]


# 2-D Arrays:  containing 2arrays with two values
import numpy as np 
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)                               # output = [[1 2 3]  [4 5 6]]


# 3-D Arrays: we will create a 3-D Array with two 2-D Arrays.
import numpy as np
array3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(array3)                                   # output = [ [[1 2][3 4]] [[5 6][7 8]] ]

# check how many dimension the array have: ndim attribute 
import numpy as np
array_D0 =np.array(42)
array_D1 =np.array([1,2,3,4,5])
array_D2 =np.array([[1,2,3],[4,5,6]])
array_D3 =np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print("array_D0 = ",array_D0.ndim) # array_D0 = 0
print("array_D1 = ",array_D1.ndim) # array_D0 = 1
print("array_D2 = ",array_D2.ndim) # array_D0 = 2
print("array_D3 = ",array_D3.ndim) # array_D0 = 3


# Create an array with 5 dimensions and  verify that it has 5 dimensions
import numpy as np 
array4 = np.array([1,2,3,4,5], ndmin=5)
print(array4)                               # output = [[[[[1 2 3 4 5]]]]]
print('number of dimension', array4.ndim)   # output = number of dimension 5


























