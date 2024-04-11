from tkinter import *
import tkinter as tk
from tkinter import ttk
from Student import Student


def show_table():
    
    def fill(students):
        for student in students:
            tree.insert(parent="", index="end", text="1", values=(student.__name, student.__surname, student.__group, student.__gender, student.__birth_year))  
   
    # Создание графического интерфейса
    window = tk.Tk()
    window.title("Таблица")
    window.geometry("700x300")
    
    

    # Создание Treeview
    tree = ttk.Treeview(window)

    # Определение столбцов таблицы
    tree["columns"] = ("Surname", "Name", "Group", "Gender", "Birth_year")

    # Настройка столбцов
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Surname", width=100,anchor="center")
    tree.column("Name", width=50,anchor="center")
    tree.column("Group", width=100,anchor="center")
    tree.column("Gender", width=100,anchor="center")
    tree.column("Birth_year", width=100,anchor="center")

    # Создание заголовков столбцов
    tree.heading("Surname", text="Фамилия")
    tree.heading("Name", text="Имя")
    tree.heading("Group", text="Группа")
    tree.heading("Gender", text="Пол")
    tree.heading("Birth_year", text="Год рождения")

    # Добавление данных в таблицу
    fill(students)
    # Размещение таблицы на окне
    tree.pack(fill="both", expand=True)

def add_student():    
    def confirm(students):
        students.append(Student(nameinput.get(),surnameinput.get(),groupinput.get(),genderinput.get(),birth_dateinput.get()))
        window.destroy()
    
    window=tk.Tk()
    window.title("Добавление студента")
    window.geometry("400x300")
    
    name=Label(window,text="Имя")
    nameinput=Entry(window, bg="white")
    name.pack()
    nameinput.pack()
    
    surname=Label(window,text="Фамилия")
    surnameinput=Entry(window, bg="white")
    surname.pack()
    surnameinput.pack()
    
    group=Label(window,text="Группа")
    groupinput=Entry(window, bg="white")
    group.pack()
    groupinput.pack()
    
    gender=Label(window,text="Пол")
    genderinput=Entry(window, bg="white")
    gender.pack()
    genderinput.pack()
    
    birth_date=Label(window,text="Год рождения")
    birth_dateinput=Entry(window, bg="white")
    birth_date.pack()
    birth_dateinput.pack()
    
    done_btn=Button(window,text="Добавить",bg="#345beb", font=40,fg='white', command=lambda: confirm(students))
    done_btn.pack(pady=(10,0))

    window.mainloop()

def show_gender():
    group_counts = {}  # Словарь для подсчета количества девушек и парней в каждой группе

    # Подсчет количества девушек и парней в каждой группе
    for student in students:
        group = student.group
        gender = student.gender

        if group not in group_counts:
            group_counts[group] = {"Male": 0, "Female": 0}

        group_counts[group][gender] += 1

    window = tk.Tk()
    window.geometry("300x200")
    window.title("Количество студентов по группам и полу")

    # Создание виджета прокрутки
    scrollbar = ttk.Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Создание виджета Text для отображения списка
    text = tk.Text(window, yscrollcommand=scrollbar.set)
    text.pack(fill=tk.BOTH, expand=True)

    # Привязка прокрутки к виджету Text
    scrollbar.config(command=text.yview)

    # Вывод количества девушек и парней в каждой группе
    for group, counts in group_counts.items():
        text.insert(tk.END, f"Группа: {group}\n")
        text.insert(tk.END, f"Количество девушек: {counts['Female']}\n")
        text.insert(tk.END, f"Количество парней: {counts['Male']}\n")
        text.insert(tk.END, "----------------------\n")

    # Запрещаем редактирование текста
    text.config(state=tk.DISABLED)

    # Запуск главного цикла окна
    window.mainloop()


def show_students_by_birth_year(students, year):
   
    # Создание нового окна для отображения результатов
    result_window = tk.Tk()
    result_window.geometry("500x400")
    result_window.title("Студенты по году рождения")

    # Создание виджета Treeview для отображения результатов
    treeview = ttk.Treeview(result_window)
    treeview.pack(fill=tk.BOTH, expand=True)

    # Определение столбцов таблицы
    treeview["columns"] = ("group", "male_count", "female_count")
    treeview.column("#0", width=0, stretch=tk.NO)  # Скрытый столбец
    treeview.column("group", width=100, anchor=tk.W)
    treeview.column("male_count", width=100, anchor=tk.W)
    treeview.column("female_count", width=100, anchor=tk.W)

    # Определение заголовков столбцов
    treeview.heading("#0", text="")
    treeview.heading("group", text="Группа")
    treeview.heading("male_count", text="Количество парней")
    treeview.heading("female_count", text="Количество девушек")

    # Фильтрация студентов по году рождения
    filtered_students = [student for student in students if str(student.birth_year) == str(year)]

    # Создание словаря для подсчета количества мужчин и женщин в каждой группе
    group_counts = {}

    # Подсчет количества мужчин и женщин в каждой группе
    for student in filtered_students:
        group = student.group
        gender = student.gender
        if group in group_counts:
            if gender == "Мужчина":
                group_counts[group]["male_count"] += 1
            elif gender == "Женщина":
                group_counts[group]["female_count"] += 1
        else:
            if gender == "Мужчина":
                group_counts[group] = {"male_count": 1, "female_count": 0}
            elif gender == "Женщина":
                group_counts[group] = {"male_count": 0, "female_count": 1}

    # Заполнение таблицы данными о группах и количестве мужчин и женщин
    for group, counts in group_counts.items():
        treeview.insert("", tk.END, text="", values=(group, counts["male_count"], counts["female_count"]))

    # Запуск главного цикла окна
    result_window.mainloop()


def birth():
     # Получение введенного года рождения
    year = int(year.get())

    # Подсчет количества студентов на заданный год рождения
    count = sum(1 for student in students if student.birth_year == year)

    window = tk.Tk()
    window.geometry("300x200")
    window.title("Количество студентов на заданный год рождения")

    # Создание виджета Text для отображения результата
    text = tk.Text(window)
    text.pack(fill=tk.BOTH, expand=True)

    # Вывод количества студентов на заданный год рождения
    text.insert(tk.END, f"Год рождения: {year}\n")
    text.insert(tk.END, f"Количество студентов: {count}\n")

    # Запрещаем редактирование текста
    text.config(state=tk.DISABLED)

    # Запуск главного цикла окна
    window.mainloop()
       
students = [
    Student("Иван", "Смирнов", "210902", "Мужчина", 1999),
    Student("Анастасия", "Ковалева", "210903", "Женщина", 2000),
    Student("Алексей", "Петров", "210902", "Мужчина", 1998),
    Student("Екатерина", "Иванова", "210822", "Женщина", 1999),
    Student("Михаил", "Сидоров", "210903", "Мужчина", 2000),
    Student("Мария", "Смирнова", "210904", "Женщина", 1999),
]
root=Tk()

root['bg']='#fafafa'
root.title('Студенты')
root.wm_attributes('-alpha', 1)
root.geometry('700x400')

root.resizable(width=False, height=False)


canvas=Canvas(root, height=1280, width=720 )
canvas.pack()

frame=Frame(root, bg='white')
frame.place(relheight=1, relwidth=1)


title=Label(frame, text="Подсчет студентов", bg='white', font=40)
title.pack(pady=(10,0))
show_table_btn=Button(frame,text='Показатель всех студентов', bg='green',fg='white',font=40,command=show_table,width=25)
gender_btn=Button(frame,text="Количество парней/девушек", bg='green',fg='white',font=40, command=show_gender,width=25)
field=Entry(frame, bg='white')
year_btn = Button(frame, text="Год рождения", bg='green', fg='white', font=40, width=25, command=lambda: show_students_by_birth_year(students,field.get()))

add_btn=Button(frame,text="Добавить студента", bg='green', font=40,fg='white', command= add_student,width=25)
show_table_btn.pack(pady=(50,0))
gender_btn.pack(pady=(20,0) )
year_btn.pack(pady=(20,0) )
field.pack(pady=(20,0))
add_btn.pack(pady=(20,0) )


root.mainloop() 
