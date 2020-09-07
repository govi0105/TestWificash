# -*- coding:utf-8 -*-
# import requests,re,json,pyperclip,pprint
# songname = input("请输入歌名：")
# url2 = "http://music.taihe.com/search?key="+songname
# # hash ="json提取的内容"
# # url = " https://www.baidu.com"
# print(url2)
# response = requests.get(url2)
# response.encoding = 'utf-8'
# text = response.text
# print(text)
# data_str = re.findall("{.*}",text)[0]
# data_json = json.loads(data_str)['data']['lists']
# l0 =data_json[0]
# l0_name=l0['FileName']
# l0_hash=l0['FileHash']
# url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash="+l0_hash+"&mid=7d503ded41d2d3a6c1e8226013950823&platid=4"
# response_1 = requests.get(url)
# response_1.encoding = 'utf-8'
# text_1 = response_1.text
#
# # print(json.dumps(text).decode('unicode-escape'))
# print(text_1)
# pprint.pprint(l0)
# print(l0_name)
# print(l0_hash)
#     # data_str = re.findall("{.*}",text)[0]
# fa =['{ "id": "128709279" }', '{ "id": "589763190" }', '{ "id": "589763191" }', '{ "id": "120901088" }', '{ "id": "242209561" }', '{ "id": "565255296" }', '{ "id": "565316822" }', '{ "id": "565406506" }', '{ "id": "565377968" }', '{ "id": "565349936" }', '{ "id": "565338834" }', '{ "id": "565396940" }', '{ "id": "565454566" }', '{ "id": "565352310" }', '{ "id": "565455022" }', '{ "id": "565328960" }', '{ "id": "565446076" }', '{ "id": "565176810" }', '{ "id": "565386446" }']
# fk ={ "id": "128709279" }
# print(fk['id'])
import tkinter as tk
from tkinter import *
import requests,re,json,pyperclip
list_name=['Afar陈侣帆《你的》你的', '러시안블루(RussianBlue)《니꺼》니꺼 (你的)', 'AOA《Red Motion》你的,我的 (니꺼 내꺼)', '冷漠,杨小曼《你是我今生的依靠》你是我今生的依靠', '门丽《你的眼角流着我的泪》你的眼角流着我的泪', '回音哥《都给你》你的配角', 'Afar陈侣帆《你的remix》你的remix', '龙飞,门丽《亲爱的 你在哪里》亲爱的 你在哪里', '程恢弘《橙灰红(Ⅰ)》DoDo Song', '永彬 Ryan.B《你的时间里》你的时间里', '金莎《星月神话》你的嘴', '刘惜君《当我身边空无一人》你的手', '马旭成,车继铃《最远的你是我最近的爱》最远的你是我最近的爱', '电视剧情定爱琴海2004插曲_你的爱给了谁审批文号：WB19085', '魏佳艺《你的样子》你的样子', '赵鑫《你的眼角流着我的泪》你的眼角流着我的泪', '龙梅子《你的爱情像闪电》你的爱情像闪电', '曹格《Super Sunshine》你的歌', '李圣杰《关于你的歌》最近', '满文军《了解》你的歌']
list_id=['616921456', '565337910', 's/2707556aba7085c4d37b7', '123339030', '120058148', '240903672', '659834570', '130259272', '541609596', '612233765', '5414327', '257512887', '123490027', '223919', '74123554', '522782032', '264630317', '450636', '563855', '969863']
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
b1 = tk.Label(root, text=list_name[0], fg='red', font=12)
b1.grid(row=1, column=1,sticky=tk.W)
b2 = tk.Label(root, text=list_name[1], fg='red', font=12)
b2.grid(row=2, column=1,sticky=tk.W)
b3 = tk.Label(root, text=list_name[2], fg='red', font=12)
b3.grid(row=3, column=1,sticky=tk.W)
b4 = tk.Label(root, text=list_name[3], fg='red', font=12)
b4.grid(row=4, column=1,sticky=tk.W)
b5 = tk.Label(root, text=list_name[4], fg='red', font=12)
b5.grid(row=5, column=1,sticky=tk.W)
#内容第三列
c1 = tk.Label(root, text=list_id[0], fg='red', font=12)
c1.grid(row=1, column=2,sticky=tk.W)
c2 = tk.Label(root, text=list_id[1], fg='red', font=12)
c2.grid(row=2, column=2,sticky=tk.W)
c3 = tk.Label(root, text=list_id[2], fg='red', font=12)
c3.grid(row=3, column=2,sticky=tk.W)
c4 = tk.Label(root, text=list_id[3], fg='red', font=12)
c4.grid(row=4, column=2,sticky=tk.W)
c5 = tk.Label(root, text=list_id[4], fg='red', font=12)
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