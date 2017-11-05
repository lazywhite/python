# -*- coding: utf-8 -*-
import numpy as np
'''
ndarray
    rank
    axes
    ndim 维数 int
    shape 维度 tuple
    size 元素数
    dtype 每个元素的类型
        itemsize 每个元素的大小
        name 类型名称
    data 存储的所有元素

dtype
    bool
    inti 由平台决定
    float16
    float32
    float64 float 
    int8
    int16
    int32
    int64
    uint8
    uint16
    uint64
    complext64
    complext128 complex

np.set_printoptions(threshold='nan')
一个ndarray所有元素类型必须相同

array.reshape() 返回一个调整过的array, 自身不变
array.resize() 将自身调整
np.add(b)
np.sqrt(a)
np.exp(a)
np.floor(a)
np.log(a)
np.sum()
np.max(a, axis=0) # axis=0按列, axis=1按行
np.floor
np.cumsum() 累加, 元素个数与array相同
np.diff(a) 相邻元素相差
np.nonzero(a) 输出非0的元素的坐标


np.logspace
np.linspace

np.vstack((a, b) 垂直合并
np.hstack((a, b)) 水平合并
np.column_stack(a, b) 将两个1维数组合并为二维数组
np.concatenate((a, b, b, a))

np.random.random() # 一个随机float number
#a = np.random.randn(5, 3) #  5行3列
#a = np.random.randint(5, 15, size=(2, 4)) # 2行4列随机整数

np.r_
np.c_

np.newaxis

np.hsplit()
np.vsplit()

# for row in A 迭代行
# for row in A.T 迭代列
# for ele in A.flat 迭代元素
np.nan 
'''


a = np.array([1, 2, 3])
a.shape # (1, 3)
print(a)


a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a.shape)
a = np.array([1, 2, 3, 4], ndmin=2)
print(a)
a = np.array([1, 2, 3, 4], dtype=np.complex)
print(a)
a = np.array([1, 2, 3, 4], dtype=np.float)
print(a)

print(a.shape, end=' ') 
print(a.dtype.itemsize) # 数据类型的字节


# 用0填充
a = np.zeros((3, 4)) # dtype默认是np.float
print(a)

# 用随机数填充
a = np.empty((3, 4), dtype=np.int32)

# 用1填充
a = np.ones((3, 4), dtype=np.int)
print(a)

# 用序列填充
a = np.arange(12).reshape(4, 3)
print(a)

print('*' * 10)
print(a.sum(axis=0)) # 按列和
print(a.sum(axis=1)) # 按行和

a = np.arange(12) # 产生一维数组
print(a)
print(np.sin(a)) # 对array中所有元素进行操作
print(a < 6) 
print(3 * a)

'''
np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
x = np.linspace( 0, 2*np.pi, 100 )        # useful to evaluate function at lots of points
f = np.sin(x)
print x
print f

'''


A = np.array( [[1,1], 
                [0,1]] )
B = np.array( [[2,0], 
                [3,4]] )
print(A*B) # 按元素乘法
print(A.dot(B)) # 矩阵点乘

b = np.linspace(0,np.pi,2)
print(b)


def f(x, y):
    return x * y

a = np.fromfunction(f, (3, 3), dtype=np.int) # 将元素的坐标作为输入

print(a)

for i in a.flat: # 迭代所有元素
    print(i)
    
for row in a:
    print(row)
print('*' * 10)
a = np.zeros((3, 3, 3), dtype=np.int)
for row in a:
    for rrow in row:
        print(rrow)


a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.ravel()) # 扁平化
print(a.T) # 转秩矩阵

a = np.array([[1,2], [3, 4]], dtype=np.int)
print(a)
print(np.linalg.det(a)) # 求矩阵的行列式

np.linalg.inv

'''
a = np.log(np.logspace(1, 10, 3))
print a
'''

a = np.array([1, 3])
b = np.array([2, 6])
print(np.column_stack((a, b)))


'''
矩阵视图, 相当于浅拷贝
'''
c = a.view()
print(c.base is a)
print(c is a)
print(c.flags)
print(c.shape)
print(a.flags)

d = a.copy() # 深拷贝

a = np.arange(10, 20).reshape(2, 5)
a.argmax()
a.argmin() # 最小元素的下标

print(a.max(axis=1))

a = np.arange(1, 7).reshape(2, 3)
print(a[1][2]) # 1行2列
print(a[1, 2]) # 1行2列
print(a[1]) # 1行所有数


