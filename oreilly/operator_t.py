from operator import itemgetter, methodcaller, attrgetter
#  itemgetter('item')(obj) = obj['item']
#  methodcaller('method', *args)(obj) = obj.method(*args)
#  attrgetter('attr')(obj) = obj.'attr'

## itemgetter: per object need has__getitem__
## attrgetter: per object need __getattr__ 

portfolio = [   
        {'name': 'IBM', 'shares': 100, 'price': 91.1},   
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

cheap = heapq.nsmallest(3, portfolio, key=itemgetter('price'))
#cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)


#rows = [
#        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
#        ]

#rows_by_fname = sorted(rows, key=itemgetter('fname'))
#rows_by_uid = sorted(rows, key=itemgetter('uid'))
#rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
#print(rows_by_fname)
#print(rows_by_uid)
#print(rows_by_lfname)
