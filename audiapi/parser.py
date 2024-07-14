import requests
from bs4 import BeautifulSoup


def fresh_six_ads(url):
    '''Парсит первые 6 объявлений на Drom.'''

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Парсим "плитку" объявлений на странице
    ad_items = soup.find_all('div', class_="css-1f68fiz ea1vuk60", limit=6)

    result = []
    for ad in ad_items:
        temp_dict = dict() # Временный словарь для данных

        # Получаем название объявления
        try:
            title = ad.find('h3', class_="css-16kqa8y efwtv890").text.strip()
        except AttributeError:
            title = ad.find('h3', class_="css-d4igzo efwtv890").text.strip()
        finally:
            temp_dict['name'] = title
        
        # Получаем цену из объявления
        price = int(ad.find('span', attrs={"data-ftid": "bull_price"}).text.strip().replace("\xa0", ''))
        temp_dict["price"] = price

        # Получаем ссылку на объявление
        link = ad.find('a', class_="g6gv8w4 g6gv8w8 _1ioeqy90").attrs['href']
        # temp_dict["link"] = ad.attrs['href']
        temp_dict["link"] = link

        # Получаем URL-фото из объявления
        try:
            url_photo = ad.find('img', class_ = "css-9w7beg evrha4s0").attrs["src"]
        except AttributeError:
            url_photo = None
        temp_dict["url_photo"] = url_photo

        # Получаем дату размещения из объявления
        date = ad.find('div', attrs={"data-ftid": "bull_date"}).text.strip()
        temp_dict["shared_time"] = date

        result.append(temp_dict)

    return result


def avg_price(url):
    '''Считает среднюю стоимость автомобиля.'''

    prices = []
    page = 1
    while page:
        url=url + f'page{page}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_="css-1dv8s3l eyvqki91")
        # print(items)
        for i in items:
            price = int(i.find('span', attrs={"data-ftid": "bull_price"}).text.strip().replace("\xa0", ''))
            prices.append(price)
        next_page = soup.find('svg', class_="_1j1e08n9")
        if not next_page:
            break
        page += 1
    
    return round(sum(prices)/len(prices))


if __name__ == '__main__':
    url = "https://auto.drom.ru/audi/a4/generation5/restyling1/"
    print(fresh_six_ads(url))
    print(avg_price(url))
