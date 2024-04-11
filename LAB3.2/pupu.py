import requests
from bs4 import BeautifulSoup

def parse(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Ошибка при получении страницы: {e}")
        return
    
   
    images = soup.find_all('img')
    num_images = len(images)
    
    # Получение общего размера всех изображений на странице
    total_size = sum(int(img.get('size', 0)) for img in images)
    
    # Получение среднего размера изображений на странице
    avg_size = total_size / num_images if num_images > 0 else 0
    
    # Получение списка всех заголовков и подзаголовков разных уровней
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    num_headers = len(headers)
    
    
    print(f"Количество изображений на странице: {num_images}")
    print(f"Общий размер изображений на странице: {total_size} байт")
    print(f"Средний размер изображений на странице: {avg_size} байт")
    print(f"Количество заголовков и подзаголовков: {num_headers}")


url = ''  
parse(url)