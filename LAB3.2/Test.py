import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from collections import deque


def len_words(words):
    word_lengths = [len(word) for word in words]
    word_lengths_counts = Counter(word_lengths)
    lengths = list(word_lengths_counts.keys())
    frequencies = list(word_lengths_counts.values())

# Построение гистограммы
    plt.bar(lengths, frequencies)
    plt.xlabel('Длина слова')
    plt.ylabel('Частота встречаемости')
    plt.title('Гистограмма встречаемости длин слов')
    plt.show()

def create_table(words, links):
    data = {
    'Количество слов': [],
    'Количество ссылок': [], 
}
    data['Количество слов'].append(words)
    data['Количество ссылок'].append(links)
    table=pd.DataFrame(data)
    
    print(table)
    

def plot(content):
    ignore = [" ", "   ", "\n", "\t", "\r"]
    for char in ignore:
        content = ''.join([c for c in content if c != char])
    character_counts = Counter(content)
    symbols = list(character_counts.keys())
    symbols.sort()
    frequencies = list(character_counts.values())


    plt.bar(symbols, frequencies)
    plt.xlabel('Символы')
    plt.ylabel('Частота встречаемости')
    plt.title('Гистограмма частоты встречаемости символов')
    plt.show()
    
    
def create_table(words, links):
    data = {
    'Количество слов': [],
    'Количество ссылок': [], 
}
    data['Количество слов'].append(words)
    data['Количество ссылок'].append(links)
    table=pd.DataFrame(data)
    print(table)

def explore_links_with_depth(url, max_depth):
    visited = set()  # Множество уже посещенных ссылок
    queue = deque([(url, 0)])  # Очередь для обхода ссылок с указанием их уровня глубины
    level_counts = {}  # Словарь для хранения количества ссылок на каждом уровне
    words=[]

    while queue:
        current_url, depth = queue.popleft()
        
        # Проверка уровня глубины
        if depth > max_depth:
            break
        
        # Проверка, была ли ссылка уже посещена
        if current_url in visited:
            continue
        
        # Посещение текущей ссылки
        visited.add(current_url)
        print(f"Посещена ссылка: {current_url} (Уровень глубины: {depth})")
        
        # Добавление ссылки в словарь количества ссылок на текущем уровне
        level_counts.setdefault(depth, 0)
        level_counts[depth] += 1
        
        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            continue    
        text=soup.get_text()
        temp=text.split()
        words.extend(temp)
        print("Длина списка",len(words))
        
        # Исследование ссылок на странице
        links = soup.find_all('a')
        for link in links:
            next_url = link.get('href')
            if next_url and next_url.startswith('https://www.mk.ru/')and "png" not in next_url and ".jpg" not in next_url:
                queue.append((next_url, depth + 1))
       
        if queue and queue[0][1] > depth:
            # Вывод количества ссылок на предыдущем уровне
            print(f"Количество ссылок на уровне {depth}: {level_counts[depth]}")
            print(f"Количество  слов  на уровне {depth}: {len(words)}")    
            plot(words)
            len_words(words)
            create_table(len(words),level_counts[depth])
            level_counts = {}
            words=[]

# Пример использования
start_url = "https://www.mk.ru/anekdoti/"
max_depth = 4
explore_links_with_depth(start_url, max_depth)