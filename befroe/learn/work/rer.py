import tkinter as tk
import requests,re,pprint,json,pyperclip
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
# list_name =[]
# list_id =[]

def music():
    global list_name
    list_name = []
    global list_id
    list_id = []
    # global mane_m
    # mane_m = input("请输入歌名：")
    url = "http://music.taihe.com/search?key={}".format(e0.get())
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
    workListAll = soup.find_all('a', attrs={'c-tj': '{"page":"search_detail","pos":"list_song","sub":"song_name"}'})
    # pprint.pprint(workListAll)
    # pprint.pprint(workListAll)
    for i in range(len(workListAll)):
        link = workListAll[i].get('title')
        list_name.append(link)

    for i in range(len(workListAll)):
        link1 = workListAll[i].get('href')
        link = re.findall("/song/(.*)", link1)[0]
        list_id.append(link)
    for i in range(len(list_id)):
        yz = 's'
        if yz in list_id[i]:
            list_id[i] = '-----'
            # list_name[i] = "-----"
    # 内容第二列
    for i in range(len(list_name)):
        if i < 5:
            b1 = tk.Label(root, text=list_name[i], fg='#d834c3', bg="#f3cff1", font=12, width=40)
            b1.grid(row=1, column=1, sticky=tk.W)
        else:
            pass
    # 内容第三列
    for i in range(len(list_id)):
        if i < 5:
            b1 = tk.Label(root, text=list_name[i], fg='#d834c3', bg="#f3cff1", font=12, width=40)
            b1.grid(row=i+1, column=1, sticky=tk.W)
        else:
            pass
    for i in range(len(list_id)):
        if i < 5:
            c1 = tk.Label(root, text=list_id[i], fg='#1711f4', font=12)
            c1.grid(row=i+1, column=2, sticky=tk.W)
            if list_id[i] == '-----':
                e1 = tk.Label(root, text='暂无', fg='red', font=12)
                e1.grid(row=i + 1, column=4, sticky=tk.W)
                root.clipboard_clear()
                f1 = tk.Button(root, text='复制', width=8, command='暂无')
                f1.grid(row=i + 1, column=5)
            else:
                url2 = " http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172017885489808536237_1556816314412&songid=" + list_id[i]
                response = requests.get(url=url2)
                text = response.text
                data_str = re.findall("{.*}", text)[0]
                data_json = json.loads(data_str)
                # pprint.pprint(data_json)
                gename = data_json['songinfo']['title']
                gesh = data_json['songinfo']['author']
                geci = data_json['songinfo']['lrclink']
                global gequ
                gequ = data_json['bitrate']['file_link']
                # print("下载地址：" + gequ)
                # print("歌名：" + gename)
                # print("歌手：" + gesh)
                # print("歌曲ID：" + data_json['songinfo']['song_id'])
                # print("歌词：" + geci)
                e1 = tk.Label(root, text=gequ, fg='red', font=12,width=40)
                e1.grid(row=i + 1, column=4, sticky =W)
                root.clipboard_clear()
                f1 = tk.Button(root, text='复制', width=8, command=11)
                f1.grid(row=i + 1, column=5)

        else:
            pass



#     return list_name,list_id
root = tk.Tk()
root.geometry('1000x500')
root.title('歌曲下载(查找完-最大化-点击复制)')
l1 = tk.Label(root, text='歌曲搜索：', fg='green', font=12, height=2)
l1.grid(row=0, column=0)
# 顶行
e0 = tk.Entry(root, text='', width=40)
e0.grid(row=0, column=1)
d0 = tk.Button(root, text='查找', width=8, height=1, bg="Pink",command=music)
d0.grid(row=0, column=3)
for i in  range(5):
    # 内容第四列
    d1 = tk.Label(root, text='下载地址：', fg='green', font=12, height=2)
    d1.grid(row=i+1, column=3)
    # 内容第一列
    a2 = tk.Label(root, text=i+1, fg='green', font=12, height=2)
    a2.grid(row=i+1, column=0)
# d2 = tk.Label(root, text='下载地址：', fg='green', font=12, height=2)
# d2.grid(row=2, column=3)
# d3 = tk.Label(root, text='下载地址：', fg='green', font=12, height=2)
# d3.grid(row=3, column=3)
# d4 = tk.Label(root, text='下载地址：', fg='green', font=12, height=2)
# d4.grid(row=4, column=3)
# d5 = tk.Label(root, text='下载地址：', fg='green', font=12, height=2)
# d5.grid(row=5, column=3)
#内容第一列
# a2 = tk.Label(root,text='   1：',fg='green',font=12,height=2)
# a2.grid(row=1,column=0)
# a3 = tk.Label(root,text='   2：',fg='green',font=12,height=2)
# a3.grid(row=2,column=0)
# a4 = tk.Label(root,text='   3：',fg='green',font=12,height=2)
# a4.grid(row=3,column=0)
# a5 = tk.Label(root,text='   4：',fg='green',font=12,height=2)
# a5.grid(row=4,column=0)
# a5 = tk.Label(root,text='   5：',fg='green',font=12,height=2)
# a5.grid(row=5,column=0)
# 内容第六列
# f1 = tk.Button(root, text='复制', width=8, command=3213)
# f1.grid(row=1, column=5)
# f2 = tk.Button(root, text='复制', width=8, command=21321)
# f2.grid(row=2, column=5)
# f3 = tk.Button(root, text='复制', width=8, command=32132)
# f3.grid(row=3, column=5)
# f4 = tk.Button(root, text='复制', width=8, command=32143)
# f4.grid(row=4, column=5)
# f5 = tk.Button(root, text='复制', width=8, command=32143)
# f5.grid(row=5, column=5)
# def music(music_id):
#     url = " http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172017885489808536237_1556816314412&songid="+music_id
#     response = requests.get(url=url)
#     text = response.text
#     data_str = re.findall("{.*}",text)[0]
#     data_json = json.loads(data_str)
#     # pprint.pprint(data_json)
#     gename = data_json['songinfo']['title']
#     gesh = data_json['songinfo']['author']
#     geci = data_json['songinfo']['lrclink']
#     global gequ
#     gequ = data_json['bitrate']['file_link']
#     print ("下载地址："+gequ)
#     print ("歌名："+gename)
#     print ("歌手："+gesh)
#     print ("歌曲ID："+data_json['songinfo']['song_id'])
#     print ("歌词："+geci)



# e1 = tk.Label(root, text='待完善', fg='red', font=12)
# e1.grid(row=1, column=4, sticky=tk.W)
# e2 = tk.Label(root, text='待完善', fg='red', font=12)
# e2.grid(row=2, column=4, sticky=tk.W)
# e3 = tk.Label(root, text='待完善', fg='red', font=12)
# e3.grid(row=3, column=4, sticky=tk.W)
# e4 = tk.Label(root, text='待完善', fg='red', font=12)
# e4.grid(row=4, column=4, sticky=tk.W)
# e5 = tk.Label(root, text='待完善', fg='red', font=12)
# e5.grid(row=5, column=4, sticky=tk.W)


def del_muid():
    e0.delete(0,'end')
c0 = tk.Button(root,text='清除',width=8,bg="Pink",command=del_muid)
c0.grid(row=0,column=2)
root.mainloop()