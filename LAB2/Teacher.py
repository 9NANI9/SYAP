from Person import Person


class Teacher(Person):
    post=None
    experience=None
    def __init__(self,surname,birthday,faculty,post,experience):
          super().__init__(surname,birthday,faculty)
          self.post=post
          self.experience=experience
          self.role="Учитель"
    def print_info(self):
        super().print_info()
        print("Должность: ", self.post)
        print("Стаж: ", self.experience)
        print("Роль: ", self.role)
        