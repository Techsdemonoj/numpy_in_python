# Searching array: you can search an array for 
# a certain value and return the indexes that get the match.
# Using where()
import numpy as np
array1 = np.array([1,2,3,4,5,4,4])
array2 = np.where(array1==4)
print(array2)


# Now we will fing the indexes where the value number are even.
import numpy as np
array3 = np.array([1,2,3,4,5,6,7,8])
array4 = np.where(array3%2 ==0)
print(array4)


# Now we will fing the indexes where the value number are odd.
import numpy as np
array3 = np.array([1,2,3,4,5,6,7,8])
array4 = np.where(array3%2 ==1)
print(array4)



# Searchsorted()- perform binary search in array.
# we will now find the index where the value 7 should be inserted.
import numpy as np
array5 = np.array([6,7,8,9])
array6 = np.searchsorted(array5,7)
print(array6)


# now we will search from right side
import numpy as np
array7 = np.array([6,7,8,9])
array8 = np.searchsorted(array7,7,side='right')
print(array8)


# how to search multiple values.
import numpy as np
array9 = np.array([1,3,5,7])
array10 = np.searchsorted(array9,[2,4,6])
print(array10)



























