import datetime
import csv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests




def collect_data():
    global card_old_price, card_title, card_discoun_percentage, card_new_price
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    response = requests.get(url='https://www.atbmarket.com/ru/promo/akciya-ekonomiya?city_id=19', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all('a', class_='card-sale_catalogue')

    data = []
    for card in cards:
        try:
            card_title = card.find('div', class_="one-action-tit").text.strip()
        except:
            pass

        try:
            card_discount_percentage = card.find('div', class_='one-action-sale-perc').text.strip()
        except:
            card_discount_percentage = "No data!"
            pass

        try:
            card_old_price = card.find('div', class_='one-action-was-price').text.strip()
        except:
            card_old_price = "No data!"

            pass

        card_new_price = card.find('div', class_='one-action-price-now').text.strip().replace(' ', '.')

        data.append([card_title, card_discount_percentage, card_old_price, card_new_price])

    with open(f'ATB_Kharkov_discount_{cur_time}.csv', 'w') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                'Продукт',
                'Старая цена',
                'Новая цена',
                'Процент скидки',
                'Время акции',
            ]
        )
        writer.writerows(
            data
        )

    print(f'Файл ATB_Kharkov_discount_{cur_time}.csv успешно записан!')
    return f'ATB_Kharkov_discount_{cur_time}.csv'

def main():
    collect_data()


if __name__ == '__main__':
    main()
