import numpy as np
matrix = np.zeros((10, 10), dtype = int)
matrix[:] = np.arange(1, 11)
print('Вот матрицa numpy 10 x 10, где каждая строка выглядит, как 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:\n', matrix)
