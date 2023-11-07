text = 'Введите через пробел фамилии школьников, решивших задачу по'
algebra = input(f'{text} алгебре>>> ').split()
geometry = input(f'{text} геометрии>>> ').split()
trigonometry = input(f'{text} тригонометрии>>> ').split()
if intersection := (set(algebra) & set(geometry) & set(trigonometry)):
    print('Все три задачи олимпиады решили ', ', '.join(intersection), '.', sep = '')
else:
    print('Все три задачи никто не решил.')
