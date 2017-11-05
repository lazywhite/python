# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()
# plt.clf()

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000),
                    columns=['a', 'b', 'c', 'd'])

data = data.cumsum()
# 折线图
#data.plot()

# 散点图
ax = data.plot.scatter("a", "b", color="DarkBlue", label="class A")
data.plot.scatter("a", "c", color="DarkGreen", label="class B", ax=ax)
plt.show()

