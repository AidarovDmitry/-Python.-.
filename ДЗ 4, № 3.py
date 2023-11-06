numbers = input()
numbers = numbers.split()
power = int(numbers.pop())
for i in range(len(numbers)):
    numbers[i] = int(numbers[i]) ** power
print(numbers)
