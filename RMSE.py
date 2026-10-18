import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import mean_squared_error

# 读取CSV文件
df = pd.read_csv('D:\DELL\热力图.csv')

# 分离输入输出变量
X = df[['S6']]  # 替换为你的特征名
y = df['Salt-water']  # 替换为你的目标变量名

# 定义PLS模型
pls = PLSRegression(n_components=1)  # 设置成你想要的成分数量

# 训练模型
pls.fit(X, y)

# 进行预测
y_pred = pls.predict(X)

# 计算均方误差
mse = mean_squared_error(y, y_pred)
rmse = mse*100

print(f"RMSE: {rmse}")

