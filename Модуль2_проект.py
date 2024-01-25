import pandas as pd
import matplotlib.pyplot as plt
input_df = pd.read_csv('C:\Датасет_для_проекта_по_II_модулю\Housing.csv', sep = ',')


print('Количество спален в самом дешёвом доме =', input_df.sort_values('price').iloc[0]['bathrooms'], '.', sep = '', end = '\n')

answer2 = len((input_df[input_df['bedrooms'] <= input_df['bathrooms']]).index)
print('Количество домов, в которых количество спален не больше количества ванных =', answer2, '.', sep = '', end = '\n')

answer3 = (input_df[input_df['guestroom'] == 'yes'].sort_values('price').iloc[0])['price']
print('Цена самого дешёвого дома с гостевой комнатой =', answer3, '.', sep = '', end = '\n')

df2 = input_df[(input_df['price'] > 5_000_000) | (input_df['price'] < 2_000_000)]
df3 = df2[df2['airconditioning'] == 'yes']
print('Доля домов ценой от 5*10^6 или до 2*10^6 денег, в которых есть кондиционирование воздуха =', len(df3) / len(df2), '.')


colours = ['violet', 'blue', 'green', 'yellow']
for colour, parking in enumerate(input_df['parking'].unique()):   
    df = input_df[input_df['parking'] == parking]
    plt.scatter(df['price'],
                df['area'],
                label = 'Количество парковочных мест=' + str(parking),
                c = colours[colour],
                alpha = 0.5)
plt.title('Зависимость цены квартиры от площади.')
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.legend()
plt.grid()
plt.show()
