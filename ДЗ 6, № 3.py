def maximum(numbers):
    highest = 0
    for number in numbers:
        if number > highest:
            highest = number
    return highest
l = input('Введите через пробел натуральные числа>>> ').split()
for i in range(len(l)):
    l[i] = int(l[i])
print(maximum(l))
