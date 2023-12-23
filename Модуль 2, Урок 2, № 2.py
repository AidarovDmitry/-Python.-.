import numpy as np
array_higher_7 = np.array([])
for i in range(1000):
    vector = np.random.randint(1, 10, size = 100)
    higher_7 = vector[(vector > 7)].size
    array_higher_7 = np.append(array_higher_7, higher_7)
equales_20 = array_higher_7[array_higher_7 == 20.0].size / 10
print(f'Доля числа результатов экспериментов, в которых результат равен 20%: {equales_20}%.')
