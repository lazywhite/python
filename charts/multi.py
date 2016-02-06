import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.arange(0, 22, 2)
f1, f2, f3, f4 = np.cumsum(np.random.random((4, x.size)) - 0.5, axis=1)

# It's much more convenient to just use pyplot's factory functions...
fig, ax = plt.subplots()

ax.set_title("Function performance",fontsize=14)
ax.set_xlabel("code executions",fontsize=12)
ax.set_ylabel("time(s)",fontsize=12)
ax.grid(True,linestyle='-',color='0.75')

colors = ['tomato', 'violet', 'blue', 'green']
labels = ['Thing One', 'Thing Two', 'Thing Three', 'Thing Four']
for func, color, label in zip([f1, f2, f3, f4], colors, labels):
        ax.plot(x, func, 'o', color=color, markersize=10, label=label)

        ax.legend(numpoints=1, loc='upper left')
        ax.set_xlim([0, x.max() + 1])

        fig.savefig('performance.png', dpi=100)
