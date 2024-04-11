
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, Qt
import math 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка числа")
        self.label = QLabel("Введите число")
        font =self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.inputLine = QLineEdit()
        self.inputLine.setMaxLength(10)
        self.inputLine.setPlaceholderText("Введите свое число (до 10 символов)")
        self.button = QPushButton("Проверить число")
        self.inputLine.returnPressed.connect(self.returnForLinePressed)
        self.button.clicked.connect(self.buttonPressed)
        self.resLabel = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputLine)
        layout.addWidget(self.button)
        layout.addWidget(self.resLabel)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setFixedSize(QSize(400,300))
        

    def returnForLinePressed(self):
        check = CheckNumber()
        inf = self.inputLine.text()
        print(inf)
        if '.' in inf:
            try:
                res = check.checkingNum(float(inf))
            except Exception as e:
                res="no"
        elif "j" in inf:
            try:
                complex(inf)
                res="complex"
            except Exception as e:
               print() 
        else :
            try:
                res = check.checkingNum(int(inf))
            except Exception as e:
                res="no"
        if(res == "easy"):
           self.resLabel.setText("Число простое")
        if(res == "float"):
           self.resLabel.setText("float число")
        if(res == "fib"):
           self.resLabel.setText("Число Фибоначчи")
        if(res == "complex"):
           self.resLabel.setText("Комплексное число")
        if(res == "int"):
           self.resLabel.setText("Целое")
        if(res =="no"): self.resLabel.setText("Неопределенно")
        self.inputLine.setText("")
    def buttonPressed(self):
        self.returnForLinePressed()
           
class CheckNumber:
   
    def isEasyNumber(self,number):
        num = number
        result = True
        if isinstance(num,float):
            return False
        if num < 2:
         result = True
        else:
         for i in range(2, int(math.sqrt(num)) + 1):
          if num % i == 0:
            result = False
        return result

    def isFibonachiNumber(self,number):
     num = int(number)
     result = True
     sqrt1 = int(math.sqrt(5 * (num ** 2) - 4))
     sqrt2 = int(math.sqrt(5 * (num ** 2) + 4))
     if (sqrt1 **2 == num):
      result = True
     if(sqrt2 **2 ==num):
       result = True
     else: 
       result = False
     return result
    
    def isComplexNumber(self,num):
      result = isinstance(num, complex)
      return result
    
    def isInt(self,num):
      result = isinstance(num,int)
      return result
    
    def isFloat(self,num):
      result = isinstance(num, float)
      return result
    def checkingNum(self,num):
        check = CheckNumber()
        res = ""
        easy = check.isEasyNumber(num)
        fibonachi = check.isFibonachiNumber(num)
        intin =check.isInt(num)
        floatin = check.isFloat(num)
        if(easy == True):
           res = "easy"
        elif(fibonachi == True):
           res = "fib"
        elif(complex == True):
           res = "complex"
        elif(intin == True):
           res = "int"
        elif(floatin == True):
           res = "float"
        else: res = "no"
        return res



           

app = QApplication([])
window = MainWindow()
window.show() 
app.exec()