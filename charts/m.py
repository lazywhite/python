# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x = [1,2,3,4]
y = [5,6,7,8]
color = 'red'
label = 'test'
ax.plot(x, y, 'o', color=color, markersize=20, label=label)

ax.legend(numpoints=1,loc='upper left')
#ax.set_xlim([0, 1000000])

plt.show()


#plt.plot([1,2,3,4])
#plt.ylabel('百分比')
#plt.show()
