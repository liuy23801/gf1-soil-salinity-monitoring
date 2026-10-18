import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('D:\DELL\热力图.csv')
df = pd.DataFrame(data)
print(data)

cor = df.corr(method='kendall', numeric_only=True)#这里标题不是数值书需要加一个numeric=True
print(cor)  # 输出相关系数

#选择一：person-皮尔逊相关系数
#选择二：spearman-斯皮尔曼相关系数

font = {'family': 'Times New Roman',
        'size': 6,
        }
sns.set(font_scale=0.8)
plt.rc('font',family='Times New Roman')
plt.subplots(figsize = (12,12))
sns.heatmap(cor,
            annot = True,
            vmax = 1,vmin=0,
            fmt='.2f',
            linecolor='blue',
            center=0.5,
            linewidth=0.5,

            square = True,
            xticklabels=True,
            yticklabels=True,
            cbar=True,

            cmap = "YlGnBu"


            # annot=True,  # 显示相关系数的数据
            # center=0.5,  # 居中
            # fmt='.2f',  # 只显示两位小数
            # linewidth=0.5,  # 设置每个单元格的距离
            # linecolor='blue',  # 设置间距线的颜色
            # vmin=0, vmax=1,  # 设置数值最小值和最大值
            # xticklabels=True, yticklabels=True,  # 显示x轴和y轴
            # square=True,  # 每个方格都是正方形
            # cbar=True,  # 绘制颜色条
            # cmap='coolwarm_r',  # 设置热力图颜色

            )
# 设置标题
plt.title('Salinity And Inversion Index Correlation Coefficient 3',fontsize='x-large')
plt.show()

