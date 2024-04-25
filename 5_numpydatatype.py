# Data types in python: string, integer, float,boolean,complex
# Data types in NumPy:
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for time delta
# M for datetime
# O fro object
# S for string
# U fro unicode string
# V memory allocation


# checking the data type of numpy araay - dtype
import numpy as np
array1 =np.array([1,2,3,4])
print(array1.dtype)


# checking the data type of numpy array - string
import numpy as np
array2 =np.array(['apple','bennana','cherry'])
print(array2.dtype)


# creating array with a defined data type:
import numpy as np
array3 = np.array([1,2,3,4], dtype='S')
print(array3)
print(array3.dtype)


# Now we will create an array with adata type of 4byte inetger.
import numpy as np
array4 = np.array([1,2,3,4], dtype='i4')
print(array4)
print(array4.dtype)


# if a type is given in which the elements cannot be casted then
# numpy will create error, what if a value cannot be converted
'''import numpy as np
array5 = np.array(['a','2','3'], dtype='i')
print(array5)
print(array5.dtype)'''

# converting data type on existing array - astype()
import numpy as np
array6 = np.array([1.1,2.1,3.1])
array6new = array6.astype('i')
print(array6new)
print(array6new.dtype)


# converting data type from integer to boolean
import numpy as np
array7 = np.array([1,0,3])
array7new = array6.astype(bool)
print(array7new)
print(array7new.dtype)



