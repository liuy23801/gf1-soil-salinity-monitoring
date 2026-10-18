# from PIL import Image
#
# # 打开图片文件
# image = Image.open('Kerle11.png')
#
# # 显示图片
# image.show()

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('tif转shp结果')

img = Image.open('Kerle11.png')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = Label(root, image=photo)
imglabel.grid(row=0, column=0, columnspan=3)

Label(root, text="Answer:").grid(row=1, column=0, sticky=S + N)

answerEntry = Entry(root)
btn = Button(root, text="Submit", command='submit')

answerEntry.grid(row=1, column=1)
btn.grid(row=1, column=2)

mainloop()

