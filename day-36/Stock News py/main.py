import requests
import time

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK = 'https://www.alphavantage.co/query?'
API_NEWS = 'https://newsapi.org/v2/everything?'
API_NEWS_KEY = 'YOUR_NEWS_API_KEY'
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': 'YOUR_ALPHAVANTAGE_API_KEY',
    'outputsize': 'compact',
    'datatype': 'json'
}

tsla_response = requests.get(url=API_STOCK, params=parameters)
tsla_response.raise_for_status()
data_tsla = tsla_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data_tsla.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

if difference < 0:
    up_down = '⬆️'
else:
    up_down = '⬇️'

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) >= 2:
    parameters_news = {
        "apiKey": API_NEWS_KEY,
        'qInTitle': COMPANY_NAME,
        'language': 'en'
    }
    news_response = requests.get(url=API_NEWS, params=parameters_news)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    three_articles = articles[:3]

    formatted_article_list = [
        f"{STOCK}: {up_down}{diff_percent}% \n Headline: {article['title']}. \n Brief: {article['description']} "
        for article in three_articles
    ]

    for article in formatted_article_list:
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={article}'
        telegram_response = requests.get(url=send_text)
        print(telegram_response.json())
