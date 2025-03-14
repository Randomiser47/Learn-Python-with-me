import requests
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK = 'https://www.alphavantage.co/query?'
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':'DBTH5RVYLRSJAO7D',
    'outputsize':'compact',
    'datatype':'json'
}


# tsla_response = requests.get(url=API_STOCK,params=parameters)
# print(tsla_response.status_code)
# data_tsla = tsla_response.json()

with open('Tesla_data.json', mode='r')as tsla_file:
    print(tsla_file.read())



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

