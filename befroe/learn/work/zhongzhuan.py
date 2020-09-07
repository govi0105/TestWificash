#7B5DD25B173FF821320F97510BB6E252
# import hashlib
# t = 51774335
# sha = hashlib.sha1(b'51774335').hexdigest()
# print(sha)
# -*- coding: utf-8 -*-
import tkinter as tk
import requests,re,pprint
from bs4 import BeautifulSoup
def music():
    mane_m = input("请输入歌名：")
    url ="http://music.taihe.com/search?key="+ mane_m
    # headers= {"Content-Type":"text/html","charset":"UTF-8"}
    r = requests.get(url)
    r.encoding = "utf-8"
    # text = r.text
    soup = BeautifulSoup(r.text,"lxml")
    # print(soup.decode('utf-8'))
    # print(soup.div)
    # print(soup.a['title'])
    #workList=soup.find('div',attrs={'class':'li-wrapper'})
    # # print(workList)
    workListAll=soup.find_all('a',attrs={'c-tj':'{"page":"search_detail","pos":"list_song","sub":"song_name"}'})
    # pprint.pprint(workListAll)
    pprint.pprint(workListAll)
    list_name = []
    list_id = []
    for i in range(len(workListAll)):
        link = workListAll[i].get('title')
        list_name.append(link)
    print(list_name)
    for i in range(len(workListAll)):
        link1 = workListAll[i].get('href')
        link= re.findall("/song/(.*)", link1)[0]
        list_id.append(link)
    print(list_id)

# list_1= re.findall("href={.*}", workListAll)
# print(list_1)
# data_json = json.loads(soup)
# pprint.pprint(data_json)
# print(soup.a.get('title'))
# print(soup.a.attrs)
    for i in range(len(list_id)):
        yz ='s'
    if yz in list_id[i]:
        list_id[i]='-----'
        list_name[i]="-----"
root = tk.Tk()

root.geometry('900x500')
root.title('歌曲下载(查找完-最大化-点击复制)')
l1 = tk.Label(root,text='歌曲搜索：',fg='green',font=12,height=2)
l1.grid(row=0,column=0)
e1 = tk.Entry(root,text='',width=40)
e1.grid(row=0,column=1)
#内容第一列
a2 = tk.Label(root,text='   1：',fg='green',font=12,height=2)
a2.grid(row=1,column=0)
a3 = tk.Label(root,text='   2：',fg='green',font=12,height=2)
a3.grid(row=2,column=0)
a4 = tk.Label(root,text='   3：',fg='green',font=12,height=2)
a4.grid(row=3,column=0)
a5 = tk.Label(root,text='   4：',fg='green',font=12,height=2)
a5.grid(row=4,column=0)
a5 = tk.Label(root,text='   5：',fg='green',font=12,height=2)
a5.grid(row=5,column=0)

#内容第二列
b1 = tk.Label(root, text=list_name[0], fg='#d834c3',bg="#f3cff1",font=12)
b1.grid(row=1, column=1,sticky=tk.W)
b2 = tk.Label(root, text=list_name[1], fg='#d834c3', font=12)
b2.grid(row=2, column=1,sticky=tk.W)
b3 = tk.Label(root, text=list_name[2], fg='#d834c3', font=12)
b3.grid(row=3, column=1,sticky=tk.W)
b4 = tk.Label(root, text=list_name[3], fg='#d834c3', font=12)
b4.grid(row=4, column=1,sticky=tk.W)
b5 = tk.Label(root, text=list_name[4], fg='#d834c3', font=12)
b5.grid(row=5, column=1,sticky=tk.W)
#内容第三列
c1 = tk.Label(root, text=list_id[0], fg='#1711f4', font=12)
c1.grid(row=1, column=2,sticky=tk.W)
c2 = tk.Label(root, text=list_id[1], fg='#1711f4', font=12)
c2.grid(row=2, column=2,sticky=tk.W)
c3 = tk.Label(root, text=list_id[2], fg='#1711f4', font=12)
c3.grid(row=3, column=2,sticky=tk.W)
c4 = tk.Label(root, text=list_id[3], fg='#1711f4', font=12)
c4.grid(row=4, column=2,sticky=tk.W)
c5 = tk.Label(root, text=list_id[4], fg='#1711f4', font=12)
c5.grid(row=5, column=2,sticky=tk.W)
#内容第四列
d0 = tk.Button(root,text='查找',width=8,height=1,bg="Pink",command=42343)
d0.grid(row=0,column=3,sticky=tk.W)
d1 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
d1.grid(row=1,column=3)
d2 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
d2.grid(row=2,column=3)
d3 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
d3.grid(row=3,column=3)
d4 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
d4.grid(row=4,column=3)
d5 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
d5.grid(row=5,column=3)

#内容第五列
e1 = tk.Label(root, text=34324, fg='red', font=12)
e1.grid(row=1, column=4,sticky=tk.W)
e2 = tk.Label(root, text=24324, fg='red', font=12)
e2.grid(row=2, column=4,sticky=tk.W)
e3 = tk.Label(root, text=24324, fg='red', font=12)
e3.grid(row=3, column=4,sticky=tk.W)
e4 = tk.Label(root, text=24324, fg='red', font=12)
e4.grid(row=4, column=4,sticky=tk.W)
e5 = tk.Label(root, text=24324, fg='red', font=12)
e5.grid(row=5, column=4,sticky=tk.W)
#内容第六列
f1 = tk.Button(root, text='复制', width=8, command=3213)
f1.grid(row=1, column=5)
f2 = tk.Button(root, text='复制', width=8, command=21321)
f2.grid(row=2, column=5)
f3 = tk.Button(root, text='复制', width=8, command=32132)
f3.grid(row=3, column=5)
f4= tk.Button(root, text='复制', width=8, command=32143)
f4.grid(row=4, column=5)
f5= tk.Button(root, text='复制', width=8, command=32143)
f5.grid(row=5, column=5)


def del_muid():
    e1.delete(0,'end')
c0 = tk.Button(root,text='清除',width=8,bg="Pink",command=del_muid)
c0.grid(row=0,column=2)
root.mainloop()