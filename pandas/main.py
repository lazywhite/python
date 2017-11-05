# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

'''
import pandas as pd

pd.get_option("display.max_columns")
pd.set_option(key, value)
pd.reset_option(key)
pd.describe_option(key)
pd.option_context()

pd.date_range('20100101', '20130101', periods=6)

panel
    dataframe # size, data 均可变
        series # size不可变, data可变

DataFrame(data, index, columns, dtype, copy )
    data type
        ndarray, series, map, lists, dict, constants and also another DataFrame.

	遍历
		iteritems()
		itertuples()
		iterrows()
           
    index: 行
    columns: 列

df.index
df.columns
df.describe()
df.loc[:,["colA", "calB"]]  select a, b from table
df.loc["line label",["colA", "calB"]] select a, b from line
df.loc[["line1", "line2"],["colA", "calB"]] select a, b from line
df.iloc[[1, 2, 3], 1:3] 
df.iloc[1:3, 1:3] 
df[df.A > 8]

pd.RangeIndex(1, 10, 1)

Panel
	T
	axes
	dtypes
	empty
	ndim
	shape
	size
	values
	head()
	tail()	
	mean()
	max()
	min()
	count()
	median() 平均值
	mod()
	std()
	abs()
	prod()
	consum()
	comprod()



	sort_index() 排序
	遍历
		for item in p

selecting data
	loc() # select by label
	iloc() # select by position
	ix() #  mixed selection


统计
	pct_change()
	cov()方差
	corr()
	rank()

绘图
	plot() 折线图
	bar() 竖直方向
	barh() 水平方向
	hist()直方图
	box()
	area()
	pie()
	scatter()

数据导入
	pd.read_csv("file", names=[], skiprow=1)
        read_excel
        hdf
        sql
        json
        msgpack
        html
        stata
        pickle
        clipboard

'''

'''
从ndarray创建series
'''
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)
print(s[100])

s = pd.Series(data) # 不指定index, 默认分配0到size的index

print(s)
print(s[1])
'''
从dict创建series
'''
a = {
    "key": "value",
    "key1": "value1",
    }
print(pd.Series(a))


s = pd.Series(5, index=[0, 1, 2, 3,])
print(s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)
print(s['a']) #从索引访问
print(s[0])  #从下标访问


'''
从list创建
'''
data = [['alex', 10], ['bob', 20], ['alice', 30]]
df = pd.DataFrame(data, columns=['name', 'age'])
print(df)


'''
从dict创建
'''
data = {"name":['a', 'b', 'c'], 'age':[1, 2, 3]}
d = pd.DataFrame(data, index=["line1", "line2", "line3"])


'''
从list(dict)创建
'''
data = [{"name": "alice", "age": 10}, {"name": "bob", "age": 20, "salary":100}]
d = pd.DataFrame(data)
print(d)

'''
从dict(series)创建
'''
data = {'name' : pd.Series(["bob", "mary", "alice"], index=['a', 'b', 'c']),
      'age' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
d = pd.DataFrame(data)
print(d)

d["salary"] = pd.Series([10, 30, 10], index=['a', 'b', 'c'])
print(d)

print('*' * 10)
print(d['name']) # 打印整列
'''
删除列
del d['age']
d.pop('salary')
'''
print('*' * 10)
print(d.loc["a"]) # 按索引获取某行
print(d.iloc[2]) # 按行号获取某行
print('*' * 10)
print(d)
print('*' * 10)
print(d[1:3]) # 按行号获取多行


df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df3 = pd.DataFrame([[9, 16], [17, 8]], columns = ['a','b'])

'''
df = df.append(df2) # 添加新行
print(df)

# Drop rows with label 0
df = df.drop(0) # label = 0的行会全部被删除

print(df)
'''

data = {"item1": df, "item2": df2, "item3": df3}
p = pd.Panel(data)
print(p)

'''
access item by "item name", "index", 
'''
print(p.loc["item3"])
print(p.iloc[2])
print(p['item1'])
print(p.ix[2])
print(p.major_xs(1))
## print(p.minor_xs(1))

print(p.ndim) # 维度
'''
TODO:
	print(p.size)  # 总的series数
	p.head()
	p.tail()
	print(p.describe()) 
'''
print(p.values)  # 所有元素
