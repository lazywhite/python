from datetime import datetime

c = datetime.today().date()
d = datetime.strftime(c, '%Y-%m-%d %H:%M:%S')
a = '2015-10-01 00:00:00'
b = datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
print type(d), d
print type(b), b

## get timestamp from datetime
import time
dt = datetime(2017, 03, 21)
print time.mktime(dt.timetuple())


