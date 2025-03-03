import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_cars_drom():
    url = 'https://auto.drom.ru/all/?order=add_date'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('div', attrs={'data-ftid': 'bulls-list_bull'})
    
    cars_list = []
   
    for listing in listings[:20]:
        title_tag = listing.find('a', {'data-ftid': 'bull_title'})
        title = title_tag.text.strip()
        link = title_tag['href'].strip()
        price = listing.find('span', {'data-ftid': 'bull_price'}).text.strip()
        location = listing.find('span', {'data-ftid': 'bull_location'}).text.strip()
        
        car_info = {
            'Заголовок': title,
            'Цена': price,
            'Местоположение': location,
            'Ссылка': link
        }
        

        cars_list.append(car_info)
    
    df = pd.DataFrame(cars_list)
    df.to_excel('cars.xlsx', index=False)
    print("Данные успешно записаны в файл cars.xlsx.")

if __name__ == "__main__":
    parse_cars_drom()
