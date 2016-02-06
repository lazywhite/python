# -*- coding: utf-8 -*-
def gen_img(labels=None, data_1=None, data_2=None, filename=None, title=None):
    '''
    '''
    import matplotlib
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt
   # fig, ax = plt.subplots()
   # ax.set_title(title)
    if labels is None:
        labels = labels
    length = len(labels)
    x = list(range(length))

    plt.xticks(x, labels, rotation=100)
    plt.grid(True)
    plt.plot(x, data_1, 'o', color="red", linewidth=3, label=u"中文")
    for i,j in zip(x,data_1):
            plt.annotate(str(j),xy=(i,j), verticalalignment='center') 
    if data_2 :
        plt.plot(x, data_2, '-', color='green', linewidth=3, label="line 2")
        for i,j in zip(x,data_2):
                plt.annotate(str(j),xy=(i,j), verticalalignment='center') 
    plt.legend(numpoints=1, loc='upper left')
    plt.savefig(filename)
    plt.clf()
#    plt.show()


gen_img(labels=['one', 'two', 'three', 'four'], data_1=[1,2,3,4], data_2=[5,6,7,8], title=u'K23测试', filename='test.png')

