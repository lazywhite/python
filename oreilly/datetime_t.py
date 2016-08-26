from datetime import timedelta, datetime
a = timedelta(days=2, hours=10)
b = timedelta(days=2.5, minutes=50)
c = a+b
print(c)
print(c.days)
print(c.seconds/3600)
print(c.total_seconds())


a = datetime(2000,2,29)
b = datetime(2014,10,20)
print(a+timedelta(days=1))
print(b-a)
print(datetime.today())
text = '2014/10/2'
y = datetime.strptime(text, '%Y/%m/%d')
print(y)
print(y.strftime('%Y-%m-%d'))
