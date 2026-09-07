import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print("Old array : ", arr)
#using the reshaping method and passing the new shape i.e., 3 x 3 (3D) from 1 x 1 (1D)
arr_new = arr.reshape(3,3)
print("New Reshaped array :\n", arr_new)

using_reshape = arr_new.reshape(-1)
print("We can also flatten any higher Dimension array to 1d.")
print("Using reshape(): ", using_reshape)
print("Using flatten(): ", arr_new.flatten())
print("Using ravel():   ", arr_new.ravel())