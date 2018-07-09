def get_essential_index(stock_datas,head_len):
    indexSet=[]
    for key in stock_datas.keys():
        for idx in range(head_len,len(stock_datas[key])-1):
            date=stock_datas[key][idx][0]
            if(float(stock_datas[key][idx-1][4])!=0):
                up=float(stock_datas[key][idx][4])/float(stock_datas[key][idx-1][4])
                if up>1.2:
                    if up<0.7:
                        continue
                    if up>1.3:
                        continue
                    index={'key':key,'idx':idx,'date':date}
                    indexSet.append(index)
    return indexSet

def get_essential_index_today(stock_datas,head_len):
    indexSet=[]
    for key in stock_datas.keys():
        for idx in range(head_len,len(stock_datas[key])):
            date=stock_datas[key][idx][0]
            if(float(stock_datas[key][idx-1][4])!=0):
                up=float(stock_datas[key][idx][4])/float(stock_datas[key][idx-1][4])
                if up>1.2:
                    if up<0.7:
                        continue
                    if up>1.3:
                        continue
                    index={'key':key,'idx':idx,'date':date}
                    indexSet.append(index)
    return indexSet