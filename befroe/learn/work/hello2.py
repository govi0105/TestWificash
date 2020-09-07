# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#      # 注意前一行 'end' 的使用
#     print(repr(x*x*x).rjust(4))
# open(file, mode='r')
from tkinter import *
root = Tk()
root.title("Entry Test")
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
#设置entry为只读属性
Entry(root, width=30,textvariable=v1, stat="readonly").pack()
v1.set("readonly")
#默认情况下下Entry的状态为normal
Entry(root, width=30,textvariable=v2).pack()
v2.set("normal")
#将输入的内容用密文的形式显示
entry = Entry(root, width=30,textvariable=v3)
v3.set("password")
entry.pack()
entry["show"] = "*"
root.mainloop()