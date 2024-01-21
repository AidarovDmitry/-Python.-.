import numpy.random as rndm
import matplotlib.pyplot as plt
data = rndm.normal(16, 2, 1000)
print('По гистограмме можно сделать вывод, основная доля участников пробежало в интервале от 50 до 325 секунд.')
plt.hist(data, color = 'red', alpha = 0.5)
plt.xlabel('Кол-во участников')
plt.ylabel('Время (с)')
plt.title('Гистограмма результатов забега на 100 м')
plt.grid()
plt.show()

