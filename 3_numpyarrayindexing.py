# 1-D Arrays indexing is the same as accesing as array elements.
import numpy as np 
array1 = np.array([1,2,3,4])
print(array1[0])  # 0th index result is = 1
print(array1[1])  # 1st index result is = 2

# we can get the 3rd element and 4th elements from adding them
import numpy as np
array2 = np.array([1,2,3,4])
print(array2[2] + array2[3]) # result =array2[2] + array2[3] =4+3=7


# 2-D Arrays: its like a rows and columns
import numpy as np
array3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd element in the 1st rows is = ", array3[0,1] ) # 2nd element in the 1st rows is =  2
print("2nd element in the 5th rows is =", array3[1,4] ) # 2nd element in the 5th rows is = 10

# 3-D Arrays:
import numpy as np
array4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array4[0,1,2])

























 