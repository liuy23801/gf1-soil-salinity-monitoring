import pandas as pd
from sklearn.cross_decomposition import PLSRegression
# 读取CSV文件
df = pd.read_csv('D:\DELL\热力图.csv')
# 分离输入和输出变量
# NDSI = df[['NDSI']]  # 根据实际特征名更改
b4 = df[['b4']]  # 根据实际特征名更改
# SI= df[['SI']]
y = df['Salt-water']  # 根据实际响应变量名更改
# 定义PLS模型
pls1 = PLSRegression(n_components=1)  # 设置成分数量
# pls2 = PLSRegression(n_components=1)  # 设置成分数量
# 训练模型
pls1.fit(b4, y)
# pls2.fit(SI, y)
# 预测
y_pred = pls1.predict(b4)
# y_pred = pls2.predict(SI)
# 输出一些模型参数
print("PLS模型中,b4的R平方为：", pls1.score(b4, y)*10)
# print("PLS模型中,NDSI的R平方为：", pls1.score(SI, y)*10)



