#折线图
import matplotlib.pyplot as plt

x1 = ['NDSI', 'NDVI', 'SI', 'SI_T', 'SAVI', 'BI', 'SI1', 'SI2',
      'SI3', 'S1', 'S2', 'S3','S5', 'S6', 'Int1', 'Int2','B1','B2','B3','B4']
# 体重
y1 = [0.1556, 0.4537, 0.5955, 0.9459, 0.1466, 0.5117
    ,0.4712,0.4519, 0.4763, 0.6774, 0.5913, 0.3374,
      0.8244,0.4344,0.4739,0.4522,0.0011,0.0062
      ,0.0934,0.03925]

# 设置画布大小
plt.figure(figsize=(12, 7))
# 设置字体
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 14}
plt.rc('font', **font1)
# 绘图
plt.plot(x1, y1, label='weight changes', linewidth=3, color='r', marker='o',
         markerfacecolor='blue', markersize=14)
# 标题
plt.title("PLSR Correlation-R²", fontproperties=font1)
# 横坐标描述
plt.xlabel('Spectral Index', fontproperties=font1)
# 纵坐标描述
plt.ylabel('Water Soluble Salt', fontproperties=font1)
# 设置数字标签
for a, b in zip(x1, y1):
    plt.text(a, b + 0.01, b, ha='center', va='bottom', fontproperties=font1)
# 设置图例
plt.legend()
plt.show()