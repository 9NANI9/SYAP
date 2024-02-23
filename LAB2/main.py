
import datetime
from Abiture import Abiture
from Student import Student
from Teacher import Teacher


person1 = Abiture("Иванов", datetime.date(2000, 5, 10), "Информатика")
person2 = Student("Макаров", datetime.date(2004, 5, 9), "Физика", 3)
person3 = Teacher("Сидоров", datetime.date(1985, 3, 22), "Математика", "Профессор", 10)

persons=[person1,person2,person3]

for person in persons:
    person.print_info()
    print()
    
min_age=input("Введите минмальный возраст: ")
max_age=input("Введите максимальный возраст: \n")
    
print("Персоны в возрасте от", min_age, "до", max_age, "лет:")
print()
for person in persons:
    current_age = datetime.datetime.now().year - person.birthday.year
    if int(min_age) <= current_age <= int(max_age):
        person.print_info()
        print()