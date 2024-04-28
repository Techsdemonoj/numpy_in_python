# Joining the numpy array: Here for this we will pass concatinate() function
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate((array1,array2))
print(array3)


# Joining of 2-D arrays along with rows(axis=1)
import numpy as np
array4 = np.array([[1,2],[3,4]])
array5 = np.array([[5,6],[7,8]])
array6 = np.concatenate((array4,array5), axis=1)
print(array6)


# Joining array using the stack() function: 
import numpy as np
array7 = np.array([1,2,3])
array8 = np.array([4,5,6])
array9 = np.stack((array7,array8),axis=1)
print(array9)


# Stacking along with rows: hstack() function
import numpy as np
array7 = np.array([1,2,3])
array8 = np.array([4,5,6])
array9 = np.hstack((array7,array8))
print(array9)


# stacking along with columns: vstack() function
import numpy as np
array7 = np.array([1,2,3])
array8 = np.array([4,5,6])
array9 = np.vstack((array7,array8))
print(array9)


# stacking along with height: dstack() function
import numpy as np
array7 = np.array([1,2,3])
array8 = np.array([4,5,6])
array9 = np.dstack((array7,array8))
print(array9)
















