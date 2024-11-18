import requests
from bs4 import BeautifulSoup
import pandas as pd
from Stock_Ticker import get_stock_tickers

stock_ticker = get_stock_tickers()

stock_data = []

print("Initializing...Please Wait..")

def getdata(symbol):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
    url = f"https://finance.yahoo.com/quote/{symbol}/"
    content = requests.get(url,headers=headers)
    soup = BeautifulSoup(content.text,"html.parser")
    stock = {
    "Symbol" : symbol,
    "Price" : soup.find("fin-streamer",{"data-field": "regularMarketPrice"}).find("span").text,
    "Previous_Close" : soup.find("fin-streamer",{"data-field":"regularMarketPreviousClose"}).text,
    "Open" : soup.find("fin-streamer",{"data-field":"regularMarketOpen"}).text,
    "Change" : soup.find("fin-streamer",{"data-field": "regularMarketChange"}).find("span").text,
    "Percent_change" : soup.find("fin-streamer",{"data-field": "regularMarketChangePercent"}).find("span").text,
    "Market_cap" : soup.find("fin-streamer",{"data-field":"marketCap"}).text,
    "Volume": soup.find("fin-streamer",{"data-field":"regularMarketVolume"}).text,
    "P_e_ratio" : soup.find("fin-streamer",{"data-field":"trailingPE"}).text
    }
    return stock


for x in stock_ticker:
    stock_data.append(getdata(x))
    print("Extracting..." + x)


stock_df = pd.DataFrame(stock_data)


print("Stocks successfully Extracted")
