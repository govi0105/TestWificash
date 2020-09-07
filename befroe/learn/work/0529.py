# -*- coding:utf-8 -*-
# import requests
# import re
# url = "https://service.danmu.youku.com/list?jsoncallback=jQuery111202280617266070326_1559110707268&mat=3&mcount=1&ct=1001&iid=1032375354&aid=302634&cid=97&lid=0&ouid=0&_=1559110707289"
# def danmu(url):
#     r = requests.get(url)
#     print(r.text)
#     sp = re.compile(r'' )
# mylist = list(range(7))
# print(mylist)
# mytuple = tuple(range(7,1,-1))
# print(mylist)
# import tkinter as tk
# # root = tk.Tk()
# # root.geometry('400x250')
# # root.title('歌曲下载')
# # l1 = tk.Label(root,text='歌 曲 ID：',fg='green',font=12,height=2)
# # l1.grid(row=0,column=0)
# # e1 = tk.Entry(root,text='',width=40)
# # e1.grid(row=0,column=1)
# # l2 = tk.Label(root,text='  歌 名 ：',fg='green',font=12,height=2)
# # l2.grid(row=1,column=0)
# # l3 = tk.Label(root,text='  歌 手 ：',fg='green',font=12,height=2)
# # l3.grid(row=2,column=0)
# # l4 = tk.Label(root,text='歌词地址：',fg='green',font=12,height=2)
# # l4.grid(row=3,column=0)
# # l5 = tk.Label(root,text='下载地址：',fg='green',font=12,height=2)
# # l5.grid(row=4,column=0)
# # b1 = tk.Button(root,text='查找',width=8,height=2)
# # b1.grid(row=5,columnspan=2)
# # root.mainloop()
list_name=['Afar陈侣帆《你的》你的', '러시안블루(RussianBlue)《니꺼》니꺼 (你的)', 'AOA《Red Motion》你的,我的 (니꺼 내꺼)', '冷漠,杨小曼《你是我今生的依靠》你是我今生的依靠', '门丽《你的眼角流着我的泪》你的眼角流着我的泪', '回音哥《都给你》你的配角', 'Afar陈侣帆《你的remix》你的remix', '龙飞,门丽《亲爱的 你在哪里》亲爱的 你在哪里', '程恢弘《橙灰红(Ⅰ)》DoDo Song', '永彬 Ryan.B《你的时间里》你的时间里', '金莎《星月神话》你的嘴', '刘惜君《当我身边空无一人》你的手', '马旭成,车继铃《最远的你是我最近的爱》最远的你是我最近的爱', '电视剧情定爱琴海2004插曲_你的爱给了谁审批文号：WB19085', '魏佳艺《你的样子》你的样子', '赵鑫《你的眼角流着我的泪》你的眼角流着我的泪', '龙梅子《你的爱情像闪电》你的爱情像闪电', '曹格《Super Sunshine》你的歌', '李圣杰《关于你的歌》最近', '满文军《了解》你的歌']
list_id=['616921456', '565337910', 's/2707556aba7085c4d37b7', '123339030', '120058148', '240903672', '659834570', '130259272', '541609596', '612233765', '5414327', '257512887', '123490027', '223919', '74123554', '522782032', '264630317', '450636', '563855', '969863']
for i in range(len(list_id)):
    yz ='s'
    if yz in list_id[i]:
        print(list_id[i])
        list_name[i]="该条无法获取"
print(list_name)