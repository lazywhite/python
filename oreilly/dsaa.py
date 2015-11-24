#!/usr/bin/env python
#==================
#unpacking a sequnce into seperate variables
#a, b, c = (1, 2, [1,2,3])
#records = [
#        ('foo', 1, 2),
#        ('bar', 'hello'),
#        ('foo', 3, 4)
#        ]
#def foo(x,y):
#    return x+y
#def bar(s):
#    print(s)

#dct={}
#dct['foo']=foo
#dct['bar']=bar

#for func, *args in records:
#    dct[func](*args)

#with open('/etc/passwd','r') as file:
#    for line in file.readlines():
#        user, *args, shell = line.split(':') # type(args) = list 
#        print(user, shell)
#========================
#import heapq

#nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
#print(heapq.nlargest(3,nums))
#print(heapq.nsmallest(3,nums))
#heapq.heapify(nums)
#print(nums)

#heapq.heappop(nums)
#heapq.heappop(nums)
#heapq.heappop(nums)

#print(nums)

#portfolio = [   
#        {'name': 'IBM', 'shares': 100, 'price': 91.1},   
#        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#        {'name': 'FB', 'shares': 200, 'price': 21.09},
#        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#        {'name': 'ACME', 'shares': 75, 'price': 115.65}
#        ]

#from operator import itemgetter
##  itemgetter('item')(obj) = obj['item']
##  methodcaller('method', *args)(obj) = obj.method(*args)
##  attrgetter('attr')(obj) = obj.'attr'
#cheap = heapq.nsmallest(3, portfolio, key=itemgetter('price'))
#cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
#print(cheap)

#======================
#heappush() and heappop() always insert and remove items from 
#a list _queue so that the first item in the list has the smallest priority
#O(logn)
#a=(1,2,3); b=(4,5) 
#a<b --> True
#same as list compare
#import heapq

#class PriorityQueue:
#    def __init__(self):
#        self._queue = []
#        self._index = 0
#    def push(self, item, priority):
#        heapq.heappush(self._queue, (-priority, self._index, item))
#        self._index += 1
#    def pop(self):
#        self._index -= 1
#        return heapq.heappop(self._queue)[-1]

#class Item:
#    def __init__(self, name):
#        self.name = name
#    def __repr__(self):
#        return 'Item: {}'.format(self.name)


#q = PriorityQueue()
#q.push(Item('foo'), 1)
#q.push(Item('bar'), 10)
#q.push(Item('spam'), 30)
#q.push(Item('grok'), 20)
#print(q._queue)
#print(q._index)
#print(q.pop())
#print(q.pop())
#print(q.pop())
#print(q.pop())
#============
# determin the most frequently occuring items in sequence
# a =Counter(list) , b = Counter(list)
#a - b
#a + b
#from collections import Counter
#words = [   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',   'my', 'eyes', "you're", 'under' ]

#word_counts = Counter(words)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
#top_three = word_counts.most_common(3)
#print(top_three)

#====================
#this script will put matched line in a fixed length deque

#from collections import deque
#def search(lines, pattern, history=5):
#    previous_line = deque(maxlen=history)
#    for line in lines:
#        if pattern in line:
#            previous_line.append(line)
#    return previous_line 
#if __name__ == '__main__':
#    with open('weakref_t.py','rt') as f:
#        for line in search(f, 'weak', 5):
#            print(line, end='')

#================
#class A:
#    def __init__(self, value):
#        self.value = value
#    def __ge__(self, obj):
#        return self.value >= obj.value
#    def __gt__(self, obj):
#        return self.value > obj.value
#    def __le__(self, obj):
#        return self.value <= obj.value
#a = A(10)
#b = A(20)
#print(a>=b)
#print(a>b)
# ===========================

#defaultdict will automatically create dictionary entries for key access
#later on
#from collections import defaultdict
### defaultdict(default_factory[,...])
### default_factory is called without arguments to produce a new value 
### and create that entry when 
### a not existed  and not binded key is accessed

#def defa():
#    return 'default value'
#c = defaultdict(defa, foo='foo')
#print(c['foo'])
#print(c['bar'])

#d = defaultdict(list)
#d['a'].append(1)
#d['a'].append(2)
#d['b'].append(1)
#print(d)
#d = defaultdict(set)
#d['a'].add(1)
#d['a'].add(2)
#d['b'].add(2)
#print(d)
#print(d['c'])
#print(d)
#====================
#OrderedDickt can exactly preserve the insertion order of items  
#it use linked list to store the order information, and consume 
#twice the size of normal dict
#from collections import OrderedDict

#d= OrderedDict()
#d['foo'] = 1
#d['bar'] = 4
#d['spam'] = 3
#d['grok'] = 2
#==========================
#prices = {
#        'ACME': 45.23,
#        'AAPL': 612.78,
#        'IBM': 205.55,
#        'HPQ': 37.20,
#        'FB': 10.75
#        }
#min_price = min(zip(prices.values(), prices.keys()))
#=================
#a = {
#        'x' : 1,
#        'y' : 2,
#        'z' : 3
#        }
#b = {
#        'w' : 10,
#        'x' : 11,
#        'y' : 2
#        }

#print(a.keys() & b.keys()) # find out same keys
#type(a.keys()) = dict_keys
#print(a.keys() - b.keys()) # findout keys in a not in b
#print(a.items() & b.items())
#a=[x for x in a.values() if x in b.values()]
#print(a)
#========================
#def dedup(items):
#    seen = set()
#    for item in items:
#        if item not in seen:
#            yield item
#            seen.add(item)

#a= [1,2,2,3,3,4,5]
#b = dedup(a)
#print(next(b))
#print(next(b))
#print(next(b))
#print(list(b))
#print(list(dedup(a)))
#b=set(a)
#print(b)
#================
#def dedupe(items, key=None):
#    seen = set()
#    for item in items:
#        val = item if key is None else key(item)
#        if val not in seen:
#            yield val
#            seen.add(val)

#a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
#b = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
#c = list(dedupe(a, key=lambda d: d['x']))
#print(b,c)
#=====================
# naming a slice
#items = [0, 1, 2, 3, 4, 5, 6]
#a = slice(2,4)
#print(items[2:4])
#print(items[a])

#s = 'hello world'
#a = slice(10,50,2)
#print(a.indices(len(s)))
#for i in range(*a.indices(len(s))):
#    print(s[i])
##===========
#from operator import itemgetter # per object need has__getitem__
# from operator import attrgetter # per object need __getattr__ 

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
## ==========================
#from operator import itemgetter
#from itertools import groupby

#rows = [
#        {'address': '5412 N CLARK', 'date': '07/01/2012'},
#        {'address': '5148 N CLARK', 'date': '07/04/2012'},
#        {'address': '5800 E 58TH', 'date': '07/02/2012'},
#        {'address': '2122 N CLARK', 'date': '07/03/2012'},
#        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
#        ]

#rows.sort(key=itemgetter('date'))
#for date, items in groupby(rows, key=itemgetter('date')):
#        print(date)
#        for i in items:
#            print('  ', i)

#from collections import defaultdict
#from pprint import pprint
#rows_by_date = defaultdict(list)
#for row in rows:
#    rows_by_date[row['date']].append(row)

#pprint(rows_by_date)
## ====================
#values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#def is_int(val):
#    try:
#        x = int(val)
#        return True
#    except ValueError:
#        return False
#ivals = list(filter(is_int,values)) #filter() create a iterator, use
# list() to get a list
#print(ivals)
## ==========
#from itertools import compress
#addresses = [
#        '5412 N CLARK',
#        '5148 N CLARK',
#        '5800 E 58TH',
#        '2122 N CLARK'
#        '5645 N RAVENSWOOD',
#        '1060 W ADDISON',
#        '4801 N BROADWAY',
#        '1039 W GRANVILLE',
#        ]
#counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

#selector = [n > 5 for n in counts]
#print(list(compress(addresses, selector))) # compress also create a iterator
## ==================
#{ key:value for key, value in prices.items() if value > 200 } # --> dict
#{ key,value for key, value in prices.items() if value > 200 } # --> list of tuple T   dict(T) get a dictionary
## ============================
## namedtuple is a replacement of dict, and is immutable
#from collections import namedtuple
#Subscriber = namedtuple('Subscriber',['addr', 'joined'])
#sub = Subscriber('a@b.com', joined='2010-10-11')
#print(sub)
#sub=sub._replace(addr='a@4.com')
#print(sub)

#Stock = namedtuple('stock',['name', 'shares', 'price', 'date', 'time'])
#stock_proto = Stock('', 0, 0.0, None, None)
#def dict_to_stock(s):
#    return stock_proto._replace(**s)
#a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
#print(dict_to_stock(a))

# ============================
#from itertools import chain

#for i in chain([1,2,3],[4,5],{'k':'v'}):
#    print(i)
# ===========================
#from itertools import repeat, islice, count
#for i in repeat('str',5):
#    print(i)

#for i in islice(count(),5,20):
#    print(i)

#a = count(5) 
#print(next(a))
# ================
#from itertools import cycle

#for i in cycle(['a','b','c']):
#    print(i) # infinity loop
# ====================
# insert elements into a list while keep that list sorted
#import bisect

#a= [10,7,9,6,8]
#a.sort()
#bisect.insort(a,7)
#print(a)
# ===========================
#from contextlib import contextmanager 

#@contextmanager 
#def f(n):
#    print('before')
#    yield 
#    print('after')

#with f(5) as f:
#    print('magic')
# ============================
#import gc
#gc.collect()
# if an object have no reference, it will be garbage collected
# if an object has only weakref, it won't 'gc'ed immediatly,
# but by periodly running garbage collector, unless by yourself

# ============================
#from collections import Iterable

#def flatten(items, ignore_type=(str, bytes)):
#    for x in items:
#        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
#            yield from x
#        else:
#            yield x
#items = [1, 2, [3, 4, 5], 6]
#print(list(flatten(items)))
# ============================
import heapq
a = [1, 4, 7]
b = [2, 5, 6]

for c in heapq.merge(a,b):
    '''require both a and b are sorted'''
    print(c)
