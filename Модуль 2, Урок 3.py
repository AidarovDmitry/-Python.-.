import pandas as pd
data = {'Product': ['Onions', 'Potatoes', 'Tomatoes', 'Carrots'],
        'Weight': [1, 44, 300, 2],
        'Expiration date': ['10.02.2024', '02.12.2023', '28.12.2023', '23.01.2024']}
df = pd.DataFrame(data)
print('Вот первые три строки таблицы:', df.head(3), sep = '\n')
print('Вот последние три строки таблицы:', df.tail(3), sep = '\n')
df.to_csv('C:\\Folder\\File.csv', index = False)
