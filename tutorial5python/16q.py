import numpy as np

A = np.random.randint(0, 20, size=(3, 3))
B = np.random.randint(0, 20, size=(3, 3))

matrix_addition = A + B
matrix_multiplication = np.dot(A, B)
transpose_result = np.transpose(matrix_multiplication)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition:\n", matrix_addition)
print("Matrix Multiplication:\n", matrix_multiplication)
print("Transpose of the Product:\n", transpose_result)
