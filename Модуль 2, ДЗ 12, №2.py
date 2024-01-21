import numpy.random as rndm
import matplotlib.pyplot as plt
X = rndm.normal(0, 1, 3000)
Y = rndm.normal(3, 4, 3000)
plt.scatter(X, Y, s = 48, c = 'brown', marker = '<', alpha = 0.3)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Рассеянная диаграмма.')
plt.grid()
plt.show()
