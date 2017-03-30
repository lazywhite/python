import re
# http://www.runoob.com/python/python-reg-expressions.html
# search: 扫描字符串， 返回第一个成功的匹配
# match: 从字符串的开始匹配


'''
\d: [0-9]
\D: [^0-9]
\s: [\f\n\r\t\v]
\S: [^\f\n\r\t\v]
\w: [A-Za-z0-9]
\W: [^A-Za-z0-9]
[^abk]: no 'a' or 'b' or 'k'
+: 1 or more
*: 0 or more

'''

st = 'abcdabbbb, abbb'

p = 'ab+'
m1 = re.search(p, st)
 
m2 = re.match(p, st) 

#print dir(m2)
print m2.group()


print m1.group()
#print dir(m1)

m = re.findall(p, st)

print m


s = "Bob Deline"
p = re.compile(r'(?P<name>\w*)\s+(?P<surname>\w*)')
g = p.match(s)
print g.groupdict()
