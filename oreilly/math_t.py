#print(round(1.2235,3))
#print(round(1.22325,-1))
#print(round(122325,-1))

# ===========
#a = 2.1
#b = 2.2
#print(a+b)
#if a+b == 4.3:
#    print('equal')

#from decimal import Decimal

#a = Decimal('2.1')
#b = Decimal('2.2')

#print(a+b)
#if (a+b) == 4.3:
#    print('false')
#elif (a+b) == Decimal('4.3'):
#    print('true')

#a = Decimal('1.3')
#b = Decimal('1.7')

#print(a/b)
#from decimal import localcontext

#with localcontext() as ctx:
#    ctx.prec = 3
#    print(a/b)

# ==================
#x = 24
#print(bin(x))
#print(oct(x))
#print(hex(x))
#print(format(x, ':>10b'))
#print(format(x, 'x'))
#print(format(x, ))
#print('the binary format of 24 is {:>10b}'.format(x))
#print(int('1010',2))
#import os
#os.chmod('math_t.py', 0o755)

# =================
#a = complex(1,2)
#b = 3-5j
#print(a+b)
# =============

#a = float('inf')
#b = float('-inf')
#c = float('nan')
#print(a,b,c)
#print(type(a), type(b), type(c))
#import math
#print(math.isinf(a))
#print(math.isinf(b))
#print(math.isnan(c))
# ==================
#from fractions import Fraction 
#a = Fraction(2,3)
#b = Fraction(4,3)

#print(a)
#print(a+b)
#print(a*b)

# =================
# numpy array, grid, matrix
# =================
#values = [1, 2, 3, 4, 5, 6]
#import random
#print(random.choice(values))
#print(random.sample(values, 2))
#random.shuffle(values)
#print(values)
#random.seed(1)
#print(random.random())
#random.seed(1)
#print(random.random())
# ====================

#from datetime import timedelta 
#a = timedelta(days=2, hours=10)
#b = timedelta(days=2.5, minutes=50)
#c = a+b
#print(c)
#print(c.days)
#print(dir(c))
#print(c.seconds/3600)
#print(c.total_seconds())

#from datetime import datetime

#a = datetime(2000,2,29)
#b = datetime(2014,10,20)
#print(a+timedelta(days=1))
#print(b-a)
#print(datetime.today())
#text = '2014/10/2'
#y = datetime.strptime(text, '%Y/%m/%d')
#print(type(y))
#print(y)
# ====================
#from dateutil import parser
#text = '2014/10/2'
#p = parser.parse(text)
#print(p)

