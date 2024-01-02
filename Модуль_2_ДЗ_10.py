import pandas as pd

data_frame = pd.read_csv('C:\Dmitry\Машинное обучение на Python\Customers.csv', sep = ';')
print('Вот люди, у которых возраст больше 30 и доход меньше 30000:')
print(data_frame[(data_frame['Age'] > 30) & (data_frame['Income'] < 30000)])
print('.')

print('Вот юристы с опытом работы больше 5 лет:')
print(data_frame[(data_frame['Work Experience'] > 5) & (data_frame['Profession'] == 'Lawyer')])
print('.')
