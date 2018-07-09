def class_calc(num):
    for i in range(1,21):
        if((num-0.7)<(i*(0.6/(20)))):
            return int((i-1)*60/(20))+70
    return 130

def SO(high, low, price):
    high=[float(i) for i in high]
    low=[float(i) for i in low]
    price=float(price)
    maxhigh=max(high)
    minlow=min(low)
    if(maxhigh==minlow):
        return 0.5
    else:
        return (price-minlow)/(maxhigh-minlow)

def RSI(price):
    price=[float(i) for i in price]
    u=0
    d=0
    for i in range(1,len(price)):
        if(price[i]>price[i-1]):
            u+=(price[i]-price[i-1])
        else:
            d+=(price[i-1]-price[i])
    u/=len(price)
    d/=len(price)
    if u+d==0:
        return 0.5
    else:
        return u/(u+d)