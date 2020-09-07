# def Copy():
#     while True:
#         readyFile=input("输入文件所在路径：")
#         writeFile=input("输入要拷贝的目录及文件名后缀：")
#         try:
#             if readyFile != None and readyFile.strip() != "" and writeFile != None and writeFile.strip() != "":
#                 with open(readyFile,"rb") as openFile,open(writeFile,"ab") as writeFile2:
#                     readyData=openFile.readlines()
#                     for rows in readyData:
#                         print(rows)
#                         writeFile2.write(rows)
#                     writeFile2.flush()
#                     writeFile2.close()
#                     openFile.close()
#                 break
#             else:
#                 print("文件路径有误，请重新输入")
#         except Exception as e:
#             print("没有找到该文件，请检查是否有此文件")
# Copy()
# import tkinter as tk
# gename = input(":")
# root = tk.Tk()
# root.geometry('400x250')
# l6 = tk.Label(root, text=gename, fg='red', font=12)
# l6.grid(row=1, column=1, sticky=W)
# import tkinter as tk
# import requests,re,pprint,json,pyperclip
# root = tk.Tk()
# root.geometry('400x250')
# root.title('歌曲下载(查找完-最大化-点击复制)')
# l1 = tk.Label(root,text='歌 曲 ID：',fg='green',font=12,height=2)
# l1.grid(row=0,column=0)
# e1 = tk.Entry(root,text='',width=40)
# e1.grid(row=0,column=1)
# l2 = tk.Label(root,text='  歌 名 ：',fg='green',font=12,height=2)
# l2.grid(row=1,column=0)
# l3 = tk.Label(root,text='  歌 手 ：',fg='green',font=12,height=2)
# l3.grid(row=2,column=0)
# l4 = tk.Label(root,text='歌词地址：',fg='green',font=12,height=2)
# l4.grid(row=3,column=0)
# l5 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
# l5.grid(row=4,column=0)
# b1 = tk.Button(root,text='查找',width=8,height=2,command=323213)
# b1.grid(row=5,columnspan=2)
# def del_muid():
#     e1.delete(0,'end')
# b2 = tk.Button(root,text='清除',width=8,command=del_muid)
# b2.grid(row=0,column=2)
# gename = 'geming'
# gesh = 'geshou'
# geci = 'geci'
# gequ = 'gequ'
#
# l6 = tk.Label(root, text=gename, fg='red', font=12)
# l6.grid(row=1, column=1,sticky=tk.W)
# l7 = tk.Label(root, text=gesh, fg='red', font=12)
# l7.grid(row=2, column=1,sticky=tk.W)
# l8 = tk.Label(root, text=geci,fg='red', font=12)
# l8.grid(row=3, column=1,sticky=tk.W)
# l9 = tk.Label(root, text=gequ,fg='red', font=12)
# l9.grid(row=4, column=1,sticky=tk.W)
# b3 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gename))
# b3.grid(row=1, column=2)
# b4 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gesh))
# b4.grid(row=2, column=2)
# b5 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(geci))
# b5.grid(row=3, column=2)
# b6 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gequ))
# b6.grid(row=4, column=2)
#
# root.mainloop()
# -*- coding:utf-8 -*-


# import tkinter
# from tkinter import ttk
#
#
# def go(*args):  # 处理事件，*args表示可变参数
#     print(comboxlist.get())  # 打印选中的值
#
#
# win = tkinter.Tk()  # 构造窗体
# comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# comboxlist["values"] = ("1", "2", "3", "4")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()

# win.mainloop()
# from tkinter import *
#
#
# root = Tk()
#
# scrolly = Scrollbar(root)
# scrolly.pack(side=RIGHT, fill=Y)
#
# mylb = Listbox(root, yscrollcommand=scrolly.set)
#
# for item in range(1, 1000):
#     mylb.insert(END, item)
#
# mylb.pack()
#
# scrolly.config(command=mylb.yview)
#
# mainloop()
#
import tkinter as tk
import requests,re,pprint,json
def music():
    global list_name
    list_name = []
    global list_id
    list_id = []
    global url
    # global mane_m
    # mane_m = input("请输入歌名：")
    url = "http://music.taihe.com/search?key={}".format(e1.get())
    print(url)
root = tk.Tk()
root.geometry('900x500')
root.title('歌曲下载(查找完-最大化-点击复制)')
l1 = tk.Label(root, text='歌曲搜索：', fg='green', font=12, height=2)
l1.grid(row=0, column=0)
e1 = tk.Entry(root,text='',width=40)
e1.grid(row=0,column=1)
d0 = tk.Button(root,text='查找',width=8,height=1,bg="Pink",command=music)
d0.grid(row=0,column=3,sticky=tk.W)
root.mainloop()