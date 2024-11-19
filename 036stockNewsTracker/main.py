# 1. Stock Price - at market close and previous day
# percentage change
# 2. when extraordinarily large, pull relevant news articles
# 3. send SMS to ourselves the change and relevant news article via Twilio

# Extra - Hard
import requests
import pandas as pd
from datetime import *

now = datetime.now()
print(now)
now += datetime.timedelta(days=1)
print(now)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

ALPHA_APIKEY = "WL7HOAOW4WBE3F6M"
ALPHA_FUNCTION = "TIME_SERIES_DAILY"
ALPHA_URL = f'https://www.alphavantage.co/query?function={ALPHA_FUNCTION}&symbol={STOCK}&interval=5min&apikey={ALPHA_APIKEY}'

r = requests.get(ALPHA_URL)
json = r.json()

prices_dict = json["Time Series (Daily)"]


# for index, rows in df.iterrows():
#     print(index)


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

