import numpy as np

arr_2d = np.array([ [1,2,3],
                    [4,5,6]
                          ])
print("The shape of the array is : ", arr_2d.shape)
print("The no. of elements in the array are : ", arr_2d.size)
print("The dimension of the array is :", arr_2d.ndim, "D")
print("The datatype of the array is : ", arr_2d.dtype)
float_arr = arr_2d.astype(float)
print(float_arr.dtype)
print(float_arr)
