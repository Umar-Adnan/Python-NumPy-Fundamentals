import numpy as np

# 1. One-Dimensional (1D) Array -> A simple list/vector
array_1d = np.array([10, 20, 30, 40])
print("1D Array:")
print(array_1d)
print("-" * 30)

# 2. Two-Dimensional (2D) Array -> A table with 2 rows and 3 columns (Matrix)
array_2d = np.array([
                    [1, 2, 3],
                    [4, 5, 6]
                            ])
print("2D Array:")
print(array_2d)
print("-" * 30)

# 3. Three-Dimensional (3D) Array -> A stack of 2D grids (Cube/Tensor)
array_3d = np.array([
                    [[1, 2], [3, 4]],   # Matrix 1 (Page 1)
                    [[5, 6], [7, 8]]    # Matrix 2 (Page 2)
                                    ])
print("3D Array:")
print(array_3d)
