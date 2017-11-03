import xlrd
import pickle
import sys
target = sys.argv[1]
aa = xlrd.open_workbook(target)

sg360 = []
tw = []
oc = []
ios = []
#nlist = zip([sg360, tw, oc], range(3))

#for m, n in  nlist:
#    sheet = aa.sheets()[n]
#    for i in xrange(sheet.nrows):
#        data = sheet.row_values(i)
#        m.append(data[1])


#with open('final', 'w') as file:
#    pickle.dump(mapping, file)
sheet = aa.sheets()[0]
for i in xrange(1, sheet.nrows):
    data =  sheet.row_values(i)
    if data[0] == 360.0:
        sg360.append(int(data[1]))
    if data[0] == u'ios':
        ios.append(int(data[1]))
    if data[0] == u'dena':
        oc.append(int(data[1]))
    if data[0] == u'denatw':
        tw.append(int(data[1]))

mapping = {}
mapping['sg360'] = sg360
mapping['tw'] = tw
mapping['oc'] = oc
mapping['ios'] = ios

with open('list', 'w') as file:
    pickle.dump(mapping, file)
