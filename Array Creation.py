import numpy as np

print("=" * 60)
print("1. FROM PYTHON LISTS / TUPLES (np.array)")
print("=" * 60)
# 1D Array
arr_1d = np.array([1, 2, 3, 4])
print("1D Array:\n", arr_1d)

# 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)


print("\n" + "=" * 60)
print("2. NUMERICAL RANGES (np.arange & np.linspace)")
print("=" * 60)
# Step-based sequence
range_arr = np.arange(0, 10, 2)
print("np.arange(0, 10, 2):\n", range_arr)

# Evenly spaced sequence over an interval
space_arr = np.linspace(0, 1, 5)
print("np.linspace(0, 1, 5):\n", space_arr)


print("\n" + "=" * 60)
print("3. PLACEHOLDER ARRAYS (zeros, ones, full, empty)")
print("=" * 60)
# Zeros
zeros_arr = np.zeros((2, 3))
print("np.zeros((2, 3)):\n", zeros_arr)

# Ones
ones_arr = np.ones((2, 2))
print("np.ones((2, 2)):\n", ones_arr)

# Full (constant value)
full_arr = np.full((2, 3), fill_value=7)
print("np.full((2, 3), 7):\n", full_arr)

# Empty (uninitialized memory)
empty_arr = np.empty((2, 2))
print("np.empty((2, 2)):\n", empty_arr)


print("\n" + "=" * 60)
print("4. SPECIAL MATRICES (np.eye & np.diag)")
print("=" * 60)
# Identity Matrix
identity_mat = np.eye(3)
print("np.eye(3) - Identity Matrix:\n", identity_mat)

# Diagonal Matrix
diag_mat = np.diag([10, 20, 30])
print("np.diag([10, 20, 30]):\n", diag_mat)


print("\n" + "=" * 60)
print("5. RANDOM NUMBER ARRAYS (np.random)")
print("=" * 60)
# Seed for reproducibility
np.random.seed(42)

# Uniform distribution between 0 and 1
rand_floats = np.random.rand(2, 3)
print("np.random.rand(2, 3):\n", rand_floats)

# Standard Normal distribution (mean=0, stdev=1)
rand_normal = np.random.randn(2, 3)
print("np.random.randn(2, 3):\n", rand_normal)

# Random Integers
rand_ints = np.random.randint(low=10, high=50, size=(2, 3))
print("np.random.randint(10, 50, size=(2, 3)):\n", rand_ints)


print("\n" + "=" * 60)
print("6. LIKE FUNCTIONS (np.zeros_like, np.ones_like)")
print("=" * 60)
source_array = np.array([[10, 20], [30, 40]])

# Creates zeros array matching the exact shape/type of source_array
zeros_like_arr = np.zeros_like(source_array)
print("Source Array:\n", source_array)
print("np.zeros_like(source_array):\n", zeros_like_arr)