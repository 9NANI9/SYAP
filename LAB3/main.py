from tkinter import *
import tkinter as tk
from tkinter import ttk
from Student import Student


def show_table():
    
    def fill(students):
        for student in students:
            tree.insert(parent="", index="end", text="1", values=(student.name, student.surname, student.group, student.gender, student.birth_year))  
   
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
    
    done_btn=Button(window,text="Добавить",bg="#345beb", font=40, command=lambda: confirm(students))
    done_btn.pack(pady=(10,0))

    window.mainloop()

def show_gender():
    def count(students):
        group_counts = {}  # Словарь для подсчета количества девушек и парней в каждой группе

        # Подсчет количества девушек и парней в каждой группе
        for student in students:
            group = student.group
            gender = student.gender

            if group not in group_counts:
                group_counts[group] = {"Male": 0, "Female": 0}

            group_counts[group][gender] += 1

        # Вывод количества девушек и парней в каждой группе
        for group, counts in group_counts.items():
            print(f"Группа: {group}")
            print(f"Количество девушек: {counts['Female']}")
            print(f"Количество парней: {counts['Male']}")
            print()

    window = Tk()
    window.title("Поиск")
    window.geometry("400x300")

    label = Label(window, text="Введите название группы", font=40)
    entry = Entry(window, bg="white")
    btn = Button(window, text="Поиск", font=40)
    label.pack(pady=(5, 0))
    entry.pack(pady=(20, 0))
    btn.pack(pady=(10, 0))
    count(students)


         
    
students=[
    Student("John", "Doe", "Group1", "Male", 1999),
    Student("Jane", "Smith", "Group1", "Female", 2000),
    Student("Alex", "Johnson", "Group2", "Male", 1998),
    Student("Emily", "Brown", "Group2", "Female", 1999),
    Student("Michael", "Davis", "Group2", "Male", 2000),
    Student("Emma", "Wilson", "Group3", "Female", 1999),
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
title.pack()
show_table_btn=Button(frame,text='Показатель всех студентов', bg='green',fg='white',font=40,command=show_table)
gender_btn=Button(frame,text="Количество парней/девушек", bg='green', font=40, command=show_gender)
year_btn=Button(frame,text="Год рождения", bg='green', font=40)
add_btn=Button(frame,text="Добавить студента", bg='green', font=40, command= add_student)
show_table_btn.pack(pady=(50,0))
gender_btn.pack(pady=(20,0) )
year_btn.pack(pady=(20,0) )
add_btn.pack(pady=(20,0) )


root.mainloop() 
