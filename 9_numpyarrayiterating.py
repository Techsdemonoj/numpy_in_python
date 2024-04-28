# Iterating Array:- Means going through the elements one by one por step by step.
# Like for Loop.

# Iterate the element of 1-D
import numpy as np
array1 = np.array([1,2,3])
for i in array1:
    print(i)
    
# Iterate the element of 2-D
import numpy as np
array2 = np.array([[1,2,3],[4,5,6]])
for i in array2:
    print(i)

# Iterate on each elements its called scaler elements
import numpy as np
array3 = np.array([[1,2,3],[4,5,6]])
for i in array3:
    for a in i:
        print(a)
        
# Iterate 3-D 
import numpy as np
array4 = np.array([[[1,2,3,],[4,5,6],[7,8,9],[10,11,12]]])
for i in array4:
    for a in i:
        for b in a:
            print(b)



# Iterating arrays using the nditer() function.
# Now we will iterate on each csaler elements.
import numpy as np
array5 = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(array5):
    print(i)
    
# Now we will Iterate with different step sizes.
import numpy as np
array6 = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(array6[:, ::2]):
    print(i)















