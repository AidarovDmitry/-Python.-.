def confirmation(surname, name, patronymic, age):
    print(f'{surname} {name} {patronymic} {age} г.р. зарегестрирован.')
sn = input('Введите фамилию>>> ')
n = input('Введите имя>>> ')
ptrnmc = input('Введите отчество>>> ')
input_age = input('Введите год рождения>>> ')
confirmation(n, sn, ptrnmc, input_age)
