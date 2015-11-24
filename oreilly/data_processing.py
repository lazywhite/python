# csv
#import csv
#from collections import namedtuple 

#with open('stock.csv') as f:
#    f_csv = csv.reader(f)
#    headers = next(f_csv)
#    print(headers)
#    Row = namedtuple('Row', headers)
#    result = []
#    a = []
#    while True:
#        line = next(f_csv,None)
#        if line is None :
#            break
#        elif line == []:
#            continue
#        else:
#            result.append(Row(*line))
#    print(result)
# ===================================
# json
#import json
#data = { 'name' : {'first':'Lili', 'last':'Sende'}, 'share' : [1,2,100], 'price' : 30 }
#a = json.dumps(data)
# dumps : serial str into json format
#print(a)
#b = json.loads(a)
# loads : deserial json into python object
#print(b)

# xml
# beautifusoup
# sqlite3
import sqlite3

stocks = [
        ('GOOG', 100, 490.1),
        ('AAPL', 50, 545.75),
        ('FB', 150, 7.45),
        ('HPQ', 75, 33.2),
        ]

db = sqlite3.connect('sqlite3.db')
c = db.cursor()
c.execute('create table portfolio (symbol text, share integer, price real)')
db.commit()
c.executemany('insert into portfolio values(?,?,?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)

db.close()

# ==============================
# base64
# binaryascii
# struct

