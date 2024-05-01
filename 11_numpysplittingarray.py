# Splitting array in numpy: it is reverse to joining,breaking the array.
# Using array_split() function.
import numpy as np
array1 = np.array([1,2,3,4,5,6])
array2 =np.array_split(array1,3)
print(array2)
# output = [array([1, 2]), array([3, 4]), array([5, 6])]


# Now we will split this array in 4 parts
import numpy as np
array1 = np.array([1,2,3,4,5,6])
array2 =np.array_split(array1,4)
print(array2)
# output = [array([1, 2]), array([3, 4]), array([5]), array([6])]


# spit into array using indexing
import numpy as np
array1 = np.array([1,2,3,4,5,6])
array2 =np.array_split(array1,3)
print(array2)                   # output =[array([1, 2]), array([3, 4]), array([5, 6])]
print(array2[0])                # output =[1 2]
print(array2[1])                # output =[3 4]
print(array2[2])                # output =[5 6]


# splitting the 2-D array
import numpy as np
array1 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
array2 = np.array_split(array1,3)
print(array2)
# output =[array([[1, 2],[3, 4]]), array([[5, 6],[7, 8]]), array([[ 9, 10],[11, 12]])]


# split the 2-D array into three 2-D array
import numpy as np
array1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
array2 = np.array_split(array1,3)
print(array2)
# output =[array([[1, 2, 3],[4, 5, 6]]), array([[ 7,  8,  9],[10, 11, 12]]), array([[13, 14, 15],[16, 17, 18]])]


# splitting the 2-D into three 2-D along with rows.
import numpy as np
array1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
array2 = np.array_split(array1,3,axis=1)
print(array2)


# alternate solutions is using the hsplit() and opposite hstack() function
import numpy as np
array1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
array2 = np.hsplit(array1,3)
print(array2)
















