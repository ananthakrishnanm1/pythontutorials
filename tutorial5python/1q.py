import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A + B
transpose_C = np.transpose(C)
print("Sum of matrices:\n", C)
print("Transpose of result:\n", transpose_C)
