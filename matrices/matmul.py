import random
import numpy as np
import time

mat1 = [
    [random.randint(-100, 100) for _ in range(200)]
    for _ in range(200)
]


mat2 = [
    [random.randint(-100, 100) for _ in range(200)]
    for _ in range(200)
]


def matmul(A, B):
    rows1 = len(A)
    cols1 = len(A[0])

    rows2 = len(B)
    cols2 = len(B[0])
    # количество столбцов первой матрицы = количеству строк второй матрицы
    if cols1 != rows2:
        raise ValueError("Number of columns in A must equal number of rows in B")
    mat = []
    for i in range(0, rows1):
        row = []
        
        for j in range(0, cols2):
            sum = 0

            for k in range(0, cols1):
                sum += A[i][k] * B[k][j]
            
            row.append(sum)
        mat.append(row) 
    return mat


start = time.time()
print(matmul(mat1, mat2))
end = time.time()
print("Время выполнения:", end - start, "секунд")


A = np.random.randint(-100, 100, size=(200, 200))
B = np.random.randint(-100, 100, size=(200, 200))

start = time.time()
print(A @ B)
end = time.time()
print("Время выполнения:", end - start, "секунд")