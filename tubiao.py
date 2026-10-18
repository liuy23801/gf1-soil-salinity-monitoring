# #折线图
# import matplotlib.pyplot as plt
#
# x1 = ['NDSI', 'NDVI', 'SI', 'SI_T', 'SAVI', 'BI', 'SI1', 'SI2',
#       'SI3', 'S1', 'S2', 'S3','S5', 'S6', 'Int1', 'Int2','B1','B2','B3','B4']
# # 体重
# y1 = [0.1556, 0.4537, 0.5955, 0.9459, 0.1466, 0.5117
#     ,0.4712,0.4519, 0.4763, 0.6774, 0.5913, 0.3374,
#       0.8244,0.4344,0.4739,0.4522,0.0011,0.0062
#       ,0.0934,0.03925]
#
# # 设置画布大小
# plt.figure(figsize=(12, 7))
# # 设置字体
# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 14}
# plt.rc('font', **font1)
# # 绘图
# plt.plot(x1, y1, label='weight changes', linewidth=3, color='r', marker='o',
#          markerfacecolor='blue', markersize=14)
# # 标题
# plt.title("Correlation-R²", fontproperties=font1)
# # 横坐标描述
# plt.xlabel('Spectral Index', fontproperties=font1)
# # 纵坐标描述
# plt.ylabel('Water Soluble Salt', fontproperties=font1)
# # 设置数字标签
# for a, b in zip(x1, y1):
#     plt.text(a, b + 0.05, b, ha='center', va='bottom', fontproperties=font1)
# # 设置图例
# plt.legend()
# plt.show()

#--------------------------------------------------------------
#柱状图
# import matplotlib.pyplot as plt
#
# # 假设这是你的数据
# labels = ['NDSI', 'NDVI', 'SI', 'SI_T', 'SAVI', 'BI', 'SI1', 'SI2', 'SI3', 'S1', 'S2', 'S3','S5', 'S6', 'Int1', 'Int2', 'B1', 'B2', 'B3', 'B4']
# values = [0.1556, 0.4537, 0.5955, 0.9459, 0.1466, 0.5117,0.4712,0.4519, 0.4763, 0.6774, 0.5913, 0.3374, 0.8244, 0.4344, 0.4739, 0.4522, 0.0011, 0.0062, 0.0934,0.03925]
#
# plt.figure(figsize=(12, 7))
# # 绘制柱状图
# plt.bar(labels, values)
#
# # 添加标题
# plt.title('Correlation-R²')
#
# # 添加横坐标的标签
# plt.xlabel('Spectral Index')
#
# # 添加纵坐标的标签
# plt.ylabel('Water Soluble Salt')
#
# # 显示网格
# # plt.grid(True)
# for a, b in zip(labels, values):
#      plt.text(a, b + 0.01, b, ha='center', va='bottom')
# # 显示图形
# plt.show()
import matplotlib.pyplot as plt
import numpy as np

# 定义数据
labels = ['NDSI', 'NDVI', 'SI', 'SI_T', 'SAVI', 'BI', 'SI1', 'SI2', 'SI3', 'S1', 'S2', 'S3','S5', 'S6', 'Int1', 'Int2', 'B1', 'B2', 'B3', 'B4']
sizes = [0.1556, 0.4537, 0.5955, 0.9459, 0.1466, 0.5117,0.4712,0.4519, 0.4763, 0.6774, 0.5913, 0.3374, 0.8244, 0.4344, 0.4739, 0.4522, 0.0011, 0.0062, 0.0934,0.03925]

# 绘制饼状图
plt.figure(figsize=(12, 7))  # 设置图像大小
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=150)
plt.title('Correlation-R²',fontsize=15)
plt.legend(fontsize=13,loc='upper right',bbox_to_anchor=(1.5, 1))
# 显示图像
plt.show()

