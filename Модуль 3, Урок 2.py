import matplotlib.pyplot as plt
x = [1, 3, 7] 
y = [2, 6, 14]
LR = 0.01
EPOCHES = 1000

omega1 = 0
b = 0
predictedF = 0

for epoch in range(EPOCHES):
    for i in range(len(x)):
        predictedF = x[i] * omega1 + b
        
        omega1 += 2 * LR * x[i] * (y[i] - predictedF)
        b += 2 * LR * (y[i] - predictedF)


print(f'Вес омега1 равен {omega1}.')
print(f'Смещкние равно {b}.')

