import numpy as np

arr = np.array([1,2,3,4,5,6,8,9,10])

print(arr[5])
print(arr[-1]) #gives the last element of the array

print(arr[1:9:2])#Slicing the array, [Start: Stop: Step]


#Fancy Indexing
print(arr[[0,6,2,6,6,8]])

#Boolean Masking
arr2 = np.arange(0,101,1)
print(arr2[arr2 % 2 == 0]) #Only picks those elements that are even throught condition
print(arr2[ arr>50 and arr<75])