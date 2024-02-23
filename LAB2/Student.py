from Person import Person

class Student(Person):
    year=None
    def __init__(self,surname,birthday,faculty,year):
         super().__init__(surname,birthday,faculty)
         self.year=year
         self.role="Студент"
    def print_info(self):
        super().print_info()
        print("Курс: ", self.year)
        print("Роль: ", self.role)