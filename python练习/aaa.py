import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文
data_dir = r'C:\Users\aa\Desktop\新建文件夹 (2)'
data_name = os.listdir(data_dir)
def file_filter(f):
    if f[-4:] in ['.txt']:
        return True
    else:
        return False
files = list(filter(file_filter, data_name))
print(files)
for i ,j in enumerate (files):
    print(j)
    base_name = os.path.splitext(j)[0]
    data_path = os.path.join(data_dir, j)
    a = np.loadtxt(data_path)
    plt.figure(dpi=120)
    sns.heatmap(data=a),#矩阵数据集，数据的index和columns分别为heatmap的y轴方向和x轴方向标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(base_name)
    plt.show()