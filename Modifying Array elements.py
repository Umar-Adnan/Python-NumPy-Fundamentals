import numpy as np

arr = np.array([10, 20, 30, 40])
arr2 = np.array([50, 60, 70, 80])
arr_2D= np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]
                        ])

#We are going to use np.insert() to insert values in the array.
#Although modifying array data is not permissbile so we make new arrays.
print("Adding elements using the np.insert() method.")
print("Axis = 0:") # Row wise insertion
arr_new1 = np.insert(arr, 1, [11,12,13,14,15], axis=0)
print(arr_new1)

print("Axis = 1:") # Column wise insertion
arr_new2 = np.insert(arr_2D, 2, [11,15,16], axis=1)
print(arr_new2)

print("Axis = None:") #Either Axis=None or axis not given, by default, the axis is 0(row wise instertion)
arr_new3 = np.insert(arr, 3, [15,16,18,19], axis = None)
print(arr_new3)
print("\n\n\n")
#=======================================================================================================
new_arry_via_append = np.append(arr, [50,60,70,80])
print("Original Array: ", arr)
print("Elements added at the end of the array using .append() method:")
print(new_arry_via_append)
print("\n\n\n")
#=============================================================================================
print("Concatenating the arrays:  ", arr, " and ", arr_new1)
arr_concatenate = np.concatenate((arr, arr_new1), axis = 0)
print("Concatenated Array: ", arr_concatenate)
print("\n\n\n")
#==============================================================================================================
arr_del = np.delete(arr, 2)
print(arr)
print("Deleted value at index 2 (30): ", arr_del)
print("\n\n\n")
#=======================================================================================================
print("Stacking the arrays : ", arr, " & ", arr2)
print("Vertical Stack: ")
print(np.vstack((arr, arr2))) #Vertical Stack(Column wise)
print("Horizontal Stack: ")
print(np.hstack((arr, arr2))) #Horizontal Stack(Row wise)
#=========================================================================================================
print("Splitting the array: ", arr)
print("Equal parts split: ", np.split((arr), 2))
print("Horizontal split: ", np.hsplit((arr), 2))
print("Vertical split: ", np.vsplit((arr_2D), 3))