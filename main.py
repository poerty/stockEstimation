import stock_name_load as snl
import stock_data_load as sdl
import essential_stock as es
import make_data as md
from sklearn.linear_model import LogisticRegression

# stock_name[k][0]=string code('086280'), stock_name[k][1]=string name
stock_names=snl.all_stock_name_load()

# execute daily
# update/write csv file to ./kospi/path
# sdl.all_stock_data_download(stock_names)
# stock data is like date/open/high/low/close/adj close/volumn

stock_datas=sdl.all_stock_data_load(stock_names)

train_essential_index=es.get_essential_index(stock_datas,14)

X,y,date=md.getXy(stock_datas,train_essential_index)

logistic_regression=LogisticRegression()
logistic_regression.fit(X,y)

full_essential_index=es.get_essential_index_today(stock_datas,14)

for item in full_essential_index:
    if(item['date']>='2018-05-01'):
        X,y=md.getSingleXy(stock_datas,item)
        prediction=logistic_regression.predict(X)
        if(prediction[0]>=105):
            #print(item,": ",prediction[0])
            print(item['key'],stock_names[[i[0] for i in stock_names].index(item['key'])][1])
            print("%s 종가 : %f-> %s 종가 : %f" %(item['date'],
                                                float(stock_datas[item['key']][item['idx']][4]),
                                                "익일",
                                                float(stock_datas[item['key']][item['idx']+1][4])))
            print("상승률 : %f" %(float(stock_datas[item['key']][item['idx']+1][4])/float(stock_datas[item['key']][item['idx']][4])))
'''
X,y,date=md.getXy(stock_datas,full_essential_index)
for i in range(0,len(X)):
    x=[]
    x.append(X[i])
    prediction=logistic_regression.predict(x)
    if(date[i]>='2018-05-01'):
        print()
        '''