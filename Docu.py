import tkinter as tk
from tkinter import filedialog

# 获取选择文件路径
# 实例化
root = tk.Tk()
root.withdraw()

# 获取文件夹路径
f_path = filedialog.askopenfilename()
print('\n获取的文件地址：', f_path)
