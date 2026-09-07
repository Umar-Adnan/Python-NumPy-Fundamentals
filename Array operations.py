import numpy as np

# Create two 1D sample arrays
a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])

print("Array A:", a)
print("Array B:", b)
print("=" * 50)

# 1. ELEMENT-WISE ARITHMETIC OPERATORS
print("1. OPERATORS (+, -, *, /, //, %, **)")
print("Addition (a + b):        ", a + b)
print("Subtraction (a - b):     ", a - b)
print("Multiplication (a * b):  ", a * b)
print("Division (a / b):        ", a / b)
print("Floor Division (a // b): ", a // b)
print("Modulus / Remainder (a % b):", a % b)
print("Exponentiation (a ** b): ", a ** b)
print("=" * 50)

# 2. EQUIVALENT NUMPY UNIVERSAL FUNCTIONS (ufuncs)
# Using explicit NumPy functions produces the exact same results as the operators above
print("2. EQUIVALENT NUMPY FUNCTIONS")
print("np.add(a, b):     ", np.add(a, b))
print("np.subtract(a, b):", np.subtract(a, b))
print("np.multiply(a, b):", np.multiply(a, b))
print("np.divide(a, b):  ", np.divide(a, b))
print("np.power(a, b):   ", np.power(a, b))
print("=" * 50)

# 3. SCALAR ARITHMETIC (Operation between Array and a single number)
print("3. SCALAR OPERATIONS")
print("a + 5: ", a + 5)
print("a * 2: ", a * 2)
print("a / 10:", a / 10)
print("=" * 50)

# 4. IN-PLACE ARITHMETIC (Modifying the array directly)
print("4. IN-PLACE MODIFICATION")
c = np.array([1, 2, 3, 4])
print("Array C = ", c)
c += 10
print("After 'c += 10':", c)
c *= 2
print("After 'c *= 2': ", c)
print("=" * 50)

# 5. COMMON MATHEMATICAL & AGGREGATION FUNCTIONS
print("5. MATHEMATICAL & STATISTICAL FUNCTIONS")
x = np.array([1, 4, 9, 16])

print("Array X:                 ", x)
print("Square Root (np.sqrt):   ", np.sqrt(x))
print("Exponential (np.exp):    ", np.exp(np.array([1, 2])))
print("Natural Log (np.log):    ", np.log(x))
print("Sum of elements:         ", x.sum())
print("Mean (Average):          ", x.mean())
print("Max value:               ", x.max())
print("Min value:               ", x.min())