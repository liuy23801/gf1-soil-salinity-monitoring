# 导入库
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel("D:\DELL\一月五号采样点表格数据.xlsx")

# print(df)
# print(df["Salt-water"])
plt.plot(df["b1"], df["Salt-water"], label='b1', linewidth=2, color='red', marker='o',
         markerfacecolor='blue', markersize=6)
plt.plot(df["b2"], df["Salt-water"], label='b2', linewidth=2, color='black', marker='o',
         markerfacecolor='yellow', markersize=6)
plt.plot(df["b3"], df["Salt-water"], label='b3', linewidth=2, color='green', marker='o',
         markerfacecolor='black', markersize=6)
plt.plot(df["b4"], df["Salt-water"], label='b4', linewidth=2, color='blue', marker='o',
         markerfacecolor='black', markersize=6)
# plt.plot(df["b2"], df["Salt-water"], label='Salt-water', linewidth=3, color='y', marker='o',
#          markerfacecolor='blue', markersize=6)
plt.xlabel("Soil Inversion")
plt.ylabel('Salt-water')
plt.title("summy of input")
plt.legend()
plt.grid()
plt.show()

