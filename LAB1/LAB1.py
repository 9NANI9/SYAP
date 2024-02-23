import pickle
import random

sequence = [[random.randint(-5, 10) for i in range(random.randint(1, 3))] for i in range(random.randint(1, 10))]
print(sequence)

# Запись последовательности
with open('F:\SHARAGA\SYAP\LAB1\sequence.bin', 'wb') as file:
    pickle.dump(sequence, file)

# Чтение последовательности
with open('F:\ШАРАГА\СЯП\LAB1\sequence.bin', 'rb') as file:
    sequence = pickle.load(file)
    


# Функция поиска четных чисел
def find_even(sequence):
    even = []
    for sublist in sequence:
        for item in sublist:  
             if item % 2 == 0:
                even.append(item)
    return even


def find_even_filter(sequence):
    even_filted=[]
    for i in sequence : 
        even_filted.append(list((filter((lambda elem : elem%2 == 0),i))))
    print(even_filted)
    return even_filted


def find_below(sequence):
    below_filted=[]
    for i in sequence:
        if(all([elem >0  for elem in i])):
            below_filted.append(i)
    print(below_filted)        
    return below_filted

find_below(sequence)

# Запись списка четных элементв в текстовый файл
with open('F:\ШАРАГА\СЯП\LAB1\even_elements.txt', 'w') as file:
    for element in  find_even(sequence):
        file.write(str(element) + '\n')
        
with open('F:\ШАРАГА\СЯП\LAB1\even_elements_filtred.txt', 'w') as file:
    for sublist in find_even_filter(sequence):
        for element in sublist:
            file.write(str(element) + '\n')
              
        
        
        