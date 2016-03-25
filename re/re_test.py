import re
# search match

st = 'abcdabbbb, abbb'

p = r'ab+'
m1 = re.search(p, st)
 
m2 = re.match(p, st) 

#print dir(m2)
print m2.group()


print m1.group()
#print dir(m1)

m = re.findall(p, st)

print m

