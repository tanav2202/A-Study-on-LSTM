import numpy as np
import pandas as pd
import os
from yahoo_fin import stock_info
import yfinance as yf

tickers = stock_info.tickers_sp500()
dataframe_names = [ticker for ticker in tickers]
dataset_dir = 'dataset'

if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

print('Web scraper starting.....')
for i in range(len(tickers)):
    historical_stock_prices = (yf.Ticker(tickers[i])).history(period='max')
    historical_stock_prices.to_csv(os.path.join(
        dataset_dir, dataframe_names[i] + '.csv'))
    # print("File", dataframe_names[i],
    #       "downloaded and stored in dataset directory")
