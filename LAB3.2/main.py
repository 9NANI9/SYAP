import pandas as pd
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt

with open(f'LAB4\My Project.html', 'r', encoding='utf-8') as file:
    data = file.read()
html = BS(data, 'html.parser')
print('ok')

links = html.find_all('a')
images = html.find_all('img')
headings = html.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
subheadings = html.find_all('p')
inputs = html.find_all('input')
divs = html.find_all('div')
words = html.get_text().split()

print('\nСсылки', len(links), '\nИзображения', len(images), '\nЗаголовки', len(headings), '\nПараграфы', len(subheadings), '\nИнтупы', len(inputs), '\nДивы', len(divs), '\nКол-во слов', len(words))
print(words)