import numpy as np

array1 = np.random.randint(0, 20, (3, 3))
array2 = np.random.randint(0, 20, (3, 3))

matrix_sum = array1 + array2

matrix_product = np.dot(array1, array2)

transpose_product = matrix_product.T

print("Array 1:\n", array1)
print("Array 2:\n", array2)
print("Matrix Sum:\n", matrix_sum)
print("Matrix Product:\n", matrix_product)
print("Transpose of Product Matrix:\n", transpose_product)