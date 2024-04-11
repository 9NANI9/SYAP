import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd




url = 'https://virotor.github.io/OAiP/annotated.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

text_elements = soup.find_all(text=True)

word_count = len(text_elements)

print(text_elements)
print(word_count)

