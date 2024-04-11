import pandas as pd
from datetime import datetime

teachers = {
    'Фамилия': ['Жидкий', 'Бабауев', 'Босый'],
    'Факультет': ['ФКП', 'Военный', 'КСИКС'],
    'Дата устройства': ['2022-01-13', '2022-01-15', '2022-01-18']
}
students = {
    'Фамилия': ['Белоусов', 'Иванов'],
    'Дата рождения': ['1990-05-15', '1985-12-01'],
    'Факультет': ['Военный', 'ФКП']
}
def add_student():
    surname = input("Введите фамилию студента: ")
    birthdate = input("Введите дату рождения студента (в формате ГГГГ-ММ-ДД): ")
    faculty = input("Введите факультет студента: ")

    students['Фамилия'].append(surname)
    students['Дата рождения'].append(birthdate)
    students['Факультет'].append(faculty)

def add_teacher():
    surname = input("Введите фамилию преподавателя: ")
    faculty = input("Введите факультет преподавателя: ")
    hire_date = input("Введите дату устройства преподавателя (в формате ГГГГ-ММ-ДД): ")

    teachers['Фамилия'].append(surname)
    teachers['Факультет'].append(faculty)
    teachers['Дата устройства'].append(hire_date)

def fill_tables():    
    print("Желаете заполнить таблицу студентов своими значениями?\n 1 - Да \n 2 - Нет")
    choice=int(input())
    if choice==1:
        while True:
            add_student()
            print("Добавить еще студента?\n 1 - Да \n 2 - Нет")
            choice=input()
            if choice==1:
                continue
            else: break
        
    print("Желаете заполнить таблицу преподавателей своими значениями?\n 1 - Да \n 2 - Нет")
    choice=int(input())
    if choice==1:
        while True:
            add_teacher()
            print("Добавить еще студента?\n 1 - Да \n 2 - Нет")
            choice=input()
            if choice==1:
                continue
            else: break

def print_tables():
    print("Студенты".center(50))
    print(students_table ,'\n')
    print("Преподаватели".center(50))
    print(teachers_table,'\n')
    print("Максимальный стаж".center(50))
    print(pivot,'\n')
    print("Преподаватели по факультету".center(50))
    print(merged_df,'\n')   
        
 
fill_tables()
    
students_table = pd.DataFrame(students)
teachers_table = pd.DataFrame(teachers)


current_date = pd.Timestamp.now().normalize()


teachers_table['Дата устройства'] = pd.to_datetime(teachers_table['Дата устройства'])
teachers_table['Месяц устройства'] = teachers_table['Дата устройства'].dt.month
teachers_table['Стаж'] = (current_date - teachers_table['Дата устройства']).dt.days
teachers_table['Месяц устройства'] = teachers_table['Дата устройства'].dt.month

#Реализация VLOOKUP
merged_df = pd.merge(students_table, teachers_table, how='left', on='Факультет')

#Реализация IF
students_table['Военная специальность'] = ['Да' if x == 'Военный' else 'Нет' for x in students_table['Факультет']]

#Реализация сводбных таблиц(Pivot tables)
pivot = teachers_table.pivot_table(index="Факультет", values="Стаж", aggfunc='max')

time=pd.to_datetime('2022-01-13')
current_date2 = pd.Timestamp.now().normalize()




print_tables()

