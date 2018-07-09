import stock_calculate as sc

def getXy(stock,indexSet):
    X=[]
    y=[]
    date=[]
    for item in indexSet:
        key=item['key']
        idx=item['idx']
        data=stock[key][idx]
        feature=[1]
        feature.append(float(data[1]))
        feature.append(float(data[2]))
        feature.append(float(data[3]))
        feature.append(float(data[4]))
        feature.append(float(data[5]))
        feature.append(float(stock[key][idx-1][4]))
        x=stock[key][idx-14:idx]
        feature.append(sc.SO([i[2] for i in x],[i[3] for i in x],stock[key][idx][4]))
        feature.append(sc.RSI([i[4] for i in x]))
        X.append(feature)
        change=float(stock[key][idx+1][4])/float(stock[key][idx][4])
        y.append(sc.class_calc(change))
        date.append(item['date'])
    return X,y,date

def getSingleXy(stock,item):
    X=[]
    y=[]
    key=item['key']
    idx=item['idx']
    data=stock[key][idx]
    feature=[1]
    feature.append(float(data[1]))
    feature.append(float(data[2]))
    feature.append(float(data[3]))
    feature.append(float(data[4]))
    feature.append(float(data[5]))
    feature.append(float(stock[key][idx-1][4]))
    x=stock[key][idx-14:idx]
    feature.append(sc.SO([i[2] for i in x],[i[3] for i in x],stock[key][idx][4]))
    feature.append(sc.RSI([i[4] for i in x]))
    X.append(feature)
    change=float(stock[key][idx+1][4])/float(stock[key][idx][4])
    y.append(sc.class_calc(change))
    return X,y