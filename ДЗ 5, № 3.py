string1 = input('Введите первую строку>>> ')
string2 = input('Введите вторую строку>>> ')
if set(string1.lower()) != set(string2.lower()):
    print('Введённые строки не являются анаграммами.')
else:
    print('Введённые строки являются анаграммами.')
