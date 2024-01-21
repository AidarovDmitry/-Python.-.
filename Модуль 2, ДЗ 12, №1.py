import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**3 - 3 * x**2 - 3 * x + 12

X = np.linspace(-12, 12, 25)
Y = function(X)
plt.plot(X, Y, color  = 'green', dashes = (5, 3), alpha = 0.5)
plt.title('Вот такая моя функция')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
