import numpy as np
array = np.random.randint(0, 1000, 144, int)
array.resize(12, 12)
print('Вот матрица 12 x 12:', array, '.', sep ='\n')
array = array.sum(axis = 0)
print('Вот массив сумм элементов матрицы в каждом столбце:', array, '.', sep ='\n')
