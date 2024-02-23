import pandas as pd
from datetime import datetime

students = {
    'Фамилия': ['Жопик', 'Пиписькин'],
    'Дата рождения': ['1990-05-15', '1985-12-01'],
    'Факультет': ['Военный', 'ФКП']
}

dframe = pd.DataFrame(students)

teachers = {
    'Фамилия': ['Иванов', 'Бабауев', 'Вонючка'],
    'Факультет': ['ФКП', 'Военный', 'КСИКС'],
    'Дата устройства': ['2022-01-13', '2022-01-15', '2022-01-18']
}

dframe2 = pd.DataFrame(teachers)


current_date = pd.Timestamp.now().normalize()


dframe2['Дата устройства'] = pd.to_datetime(dframe2['Дата устройства'])
dframe2['Месяц устройства'] = dframe2['Дата устройства'].dt.month
dframe2['Текущий стаж'] = (current_date - dframe2['Дата устройства']).dt.days

merged_df = pd.merge(dframe, dframe2, how='left', on='Факультет')

dframe['Военная специальность'] = ['Да' if x == 'Военный' else 'Нет' for x in dframe['Факультет']]
print(dframe)
print()
print(dframe2)
print()
print(merged_df)   