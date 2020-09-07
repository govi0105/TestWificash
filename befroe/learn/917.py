import tkinter as tk
import requests,re,json,pyperclip,pprint
def music():
    url = " http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172017885489808536237_1556816314412&songid={}".format(e1.get())
    response = requests.get(url=url)
    text = response.text
    print(text)
    data_str = re.findall("{.*}",text)[0]
    data_json = json.loads(data_str)
    pprint.pprint(data_json)
    gename = data_json['songinfo']['title']
    gesh = data_json['songinfo']['author']
    geci = data_json['songinfo']['lrclink']
    gequ = data_json['bitrate']['file_link']
    print ("下载地址："+gequ)
    print ("歌名："+gename)
    print ("歌手："+gesh)
    print ("歌曲ID："+data_json['songinfo']['song_id'])
    print ("歌词："+geci)
    l6 = tk.Label(root, text=gename, fg='red', font=12)
    l6.grid(row=1, column=1,sticky=tk.W)
    l7 = tk.Label(root, text=gesh, fg='red', font=12)
    l7.grid(row=2, column=1,sticky=tk.W)
    l8 = tk.Label(root, text=geci,fg='red', font=12)
    l8.grid(row=3, column=1,sticky=tk.W)
    l9 = tk.Label(root, text=gequ,fg='red', font=12)
    l9.grid(row=4, column=1,sticky=tk.W)
    b3 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gename))
    b3.grid(row=1, column=2)
    b4 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gesh))
    b4.grid(row=2, column=2)
    b5 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(geci))
    b5.grid(row=3, column=2)
    b6 = tk.Button(root, text='复制', width=8, command=pyperclip.copy(gequ))
    b6.grid(row=4, column=2)
root = tk.Tk()
root.geometry('400x250')
root.title('歌曲下载(查找完-最大化-点击复制)')
l1 = tk.Label(root,text='歌 曲 ID：',fg='green',font=12,height=2)
l1.grid(row=0,column=0)
e1 = tk.Entry(root,text='',width=40)
e1.grid(row=0,column=1)
b1 = tk.Button(root,text='查找',width=8,height=2,command=music)
b1.grid(row=5,columnspan=2)
l2 = tk.Label(root,text='  歌 名 ：',fg='green',font=12,height=2)
l2.grid(row=1,column=0)
l3 = tk.Label(root,text='  歌 手 ：',fg='green',font=12,height=2)
l3.grid(row=2,column=0)
l4 = tk.Label(root,text='歌词地址：',fg='green',font=12,height=2)
l4.grid(row=3,column=0)
l5 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
l5.grid(row=4,column=0)

def del_muid():
    e1.delete(0,'end')
b2 = tk.Button(root,text='清除',width=8,command=del_muid)
b2.grid(row=0,column=2)
# b3 = tk.Button(root,text='复制',width=8,command=pyperclip.copy(gename))
# b3.grid(row=1,column=2)
# b4 = tk.Button(root,text='复制',width=8,command=pyperclip.copy('Hello world!'))
# b4.grid(row=2,column=2)
# b5 = tk.Button(root,text='复制',width=8,command=pyperclip.copy('Hello world!'))
# b5.grid(row=3,column=2)
# b6 = tk.Button(root,text='复制',width=8,command=pyperclip.copy('Hello world!'))
# b6.grid(row=4,column=2)
root.mainloop()
# –icon=图标路径（pyinstaller -F --icon=my.ico XXXX.py）
# -F 打包成一个exe文件pyinstaller -F --icon=my.ico xxx.py
# -w 使用窗口，无控制台
# -c 使用控制台，无窗口
# -D 创建一个目录，里面包含exe以及其他一些依赖性文件