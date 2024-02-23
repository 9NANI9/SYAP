import datetime


class Person:
    surname = None
    birthday = None
    faculty = None
    role=None
    
    def __init__(self, surname, birthday, faculty):
        self.surname = surname
        self.birthday = birthday
        self.faculty = faculty
        
    def print_info(self):
        print("Фамилия:", self.surname)
        print("Дата рождения:", self.birthday)
        print("Факультет:", self.faculty)
        print("Возраст:", self.get_age())

        
    def get_age(self):
        current_year = datetime.datetime.now().year
        birth_year = self.birthday.year
        age = current_year - birth_year
        return age