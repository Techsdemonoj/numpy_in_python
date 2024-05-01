# Getting some lelements out of an exsisting array and cerate a new array is called filtering.and 
# A boolean index list is alist of boolean corresponding to indexes in the array.(True and False)
# Create a array from the element on index 0 to 2.
import numpy as np
array1 = np.array([41,42,43,44])
array2 = [True,False,True,False]
final_array = array1[array2]
print(final_array)


# now we will create a filter array.
import numpy as np
array1 =np.array([41,42,43,44])
empty_array = []
for i in array1:
    if i>42:
        empty_array.append(True)
    else:
        empty_array.append(False)
new_array = array1[empty_array]
print(empty_array)
print(new_array)




















