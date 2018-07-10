import csv

nolist=['5980','271980','145210']

def all_stock_name_load():
    x=[]
    file='stockname.csv'
    with open(file,'r') as csvfile:
        csv_reader=csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            if row[1] in nolist:
                continue
            l=[]
            l.append('{0:06d}'.format(int(row[1])))
            l.append(row[2])
            x.append(l)
    return x