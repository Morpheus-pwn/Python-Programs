import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

result = matrix1 + matrix2

transpose_result = result.T

print("Resultant Matrix:\n", result)
print("Transpose of Resultant Matrix:\n", transpose_result)