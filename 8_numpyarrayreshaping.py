# Reshaping:- means changing the shape of an array, like adding and removing the elements


# Reshaping from  1-D to 2-D
import numpy as np
array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array2 = array1.reshape(4,3)
print('Convert 1-D to 2-D: ',array2)
# outupt=  [[ 4  5  6]
#          [ 7  8  9]
#          [10 11 12]]


# Reshaping from 1-D to 3-D
import numpy as np
array3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array4 = array3.reshape(2,3,2)
print('Convert 1-D to 3-D: ',array4)
# outupt= [ [[ 1  2]
#           [ 3  4]
#           [ 5  6]]

#          [[ 7  8]
#           [ 9 10]
#           [11 12]] ]

import numpy as np
array5 = np.array([1,2,3,4,5,6,7,8,9])
array6 = array5.reshape(3,3)
print(array6)

# Return copy or view
import numpy as np
array7 = np.array ([1,2,3,4,5,6,7,8])
print(array7.reshape(2,4).base)
# output = [1 2 3 4 5 6 7 8] its means this array is view condition that why its print print original value


# Unknown dimension - you are only allowed to have one unknown dimension.
# pass -1.
import numpy as np
array8 = np.array([1,2,3,4,5,6,7,8])
array9 = array8.reshape(2,2,-1)
print(array9)  # this is called unknown dimension


# Flattening the array by converting multidimensional array in 1-D
import numpy as np
array10 = np.array([[1,2,3,4],[5,6,7,8]])
array11 = array10.reshape(-1)
print(array11)


# There are a lot of functions for changing the shpaeo of an array in numpy.
# like,ravel and also rearranging the emlements rot90,flip,fliplr,flipud.
# They all are actually comes under advanced numpy.





















 