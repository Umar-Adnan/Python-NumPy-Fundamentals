# Vectorization means to perfrom mathematical operations on an array all at once rather
# than processing element by elemenet.
# These are performed by pre-compiled, highly optimized C routines instead of standarad python loops.
# Vectorization is faster 100-1000 times than conventional Python.

import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,91,100])
print(arr*3)         #All elements multiplied by 3
print(arr/10)        #All elements divided by 10
print(arr - 20)      #All elements subtracted by 20
print(arr % 10 == 0) #Checking if all elements are divided by 10 or not, prints true or false
print(arr ** 2)      #All elements exponentiated to the power of 2