import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as pdr
from pandas_datareader import data
import fix_yahoo_finance as yf
import re
import glob
import os
import csv
import numpy as np

def delete_kospi():
    file_list = glob.glob('./kospi/*.csv')
    for file in file_list:
        os.remove(file)

def save_kospi(stock_names):
    yf.pdr_override()    
    for stock in stock_name:
        kor_name = stock[1]
        ticker = stock[0]
        df = data.get_data_yahoo(ticker + '.KS', '1996-05-06', thread=100)
        df.to_csv('./kospi/{}.csv'.format(ticker))
        print('{}.csv is saved'.format(ticker))

def reload_empty(stock_names):
    yf.pdr_override()    
    file_list = glob.glob('./kospi/*.csv')
    six_digit = re.compile('\d{6}')
    for file_name in file_list:
        file = pd.read_csv(file_name)
        if file.empty:
            print("empty file {} is updated".format(file_name))
            ticker = six_digit.findall(file_name)[0]
            _ticker = ticker + '.KS'
            tmp_df = data.get_data_yahoo(_ticker, start='1996-05-06', thread=100)
            tmp_df.to_csv(file_name)

def all_stock_data_download(stock_names):    
    delete_kospi()
    save_kospi(stock_names)
    reload_empty(stock_names)

def stock_data_load(stockCode):
    x=[]
    file="./kospi/"+stockCode+".csv"
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            x.append(row)
    return np.array(x)

def all_stock_data_load(stock_names):
    stock={}
    for code in stock_names:
        tmp=stock_data_load(code[0])
        if tmp.size!=0:
            stock[code[0]]=tmp
    return stock