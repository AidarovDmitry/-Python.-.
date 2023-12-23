import numpy as np
vector = np.random.randint(1, 10, size = 100)
print(f'В векторе {vector[(vector > 7)].size}% элементов больших 7.')
