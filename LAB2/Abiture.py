from Person import Person

class Abiture(Person):
    def __init__(self,surname,birthday,faculty):
        super().__init__(surname,birthday,faculty)
        self.role="Абитуриент"
    def print_info(self):
        super().print_info()   
        print("Роль: ", self.role) 
        
    