# -*- coding: utf-8 -*-
# the auther is cjj

# import requests
# import re
# # 第一步，获取歌曲的ids
# search_api = 'http://music.baidu.com/search'
# # 搜索关键字，传递参数，通过字典构造
# keyword = {'key': '刘德华'}
# # 发送get请求   params 是传递的get参数
# response = requests.get(search_api, params=keyword)
# # 取出html的源码
# response.encoding = 'utf-8'  # 编码转换
# html = response.text
# # 通过正则表达式获取id
# ids = re.findall(r'{&quot;id&quot;:&quot;(\d+)&quot',html)
#
# # 第二步，获取歌曲的信息
# mp3_info_api = 'http://play.baidu.com/data/music/songlink'
# data = {
#     'songIds': ','.join(ids),
#     'hq': 0,
#     'type': 'm4a,mp3',
#     'rate': '',
#     'pt': 0,
#     'flag': -1,
#     's2p': -1,
#     'prerate': -1,
#     'bwt': -1,
#     'dur': -1,
#     'bat': -1,
#     'bp': -1,
#     'pos': -1,
#     'auto': -1
# }
# # data就是 post的参数
# res = requests.post(mp3_info_api,data=data)
# # 返回值的数据是就送格式，直接调用json方法，转成字典
# info = res.json()
#
# # 第三步，去下载歌曲
# # 根据数据的结构获取歌曲的信息
# song_info = info['data']['songList']
# # 循环
# for song in song_info:
#     # 根据数据结构获取信息
#     # 歌名
#     song_name = song['songName']
#     # mp3地址
#     song_link = song['songLink']
#     # 格式
#     for_mat = song['format']
#     # 歌词地址
#     lrclink = song['lrcLink']
#     print(song_name)
#     # 下载mp3
#     if song_link: # 可能没有地址
#         song_res = requests.get(song_link) # 下载
#         # 写文件
#         with open('%s.%s' % (song_name, for_mat),'wb') as f:
#             f.write(song_res.content)  # 歌曲是二进制
#     # 下载歌词
#     if lrclink:
#         lrc_response = requests.get(lrclink)
#         # 写文件
#         with open('%s.lrc' % song_name, 'w', encoding= 'gbk') as f:
#             f.write(lrc_response.text)
# import requests
# import json
# import re
#
# '''
# 有需要Python学习资料的小伙伴吗?小编整理一套Python资料和PDF，感兴趣者可以加学习群：548377875，反正闲着也是闲着呢，不如学点东西啦~~
# '''
#
#
# def get_song(x):
#     url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery112407470964083509348_1534929985284&keyword={}&" \
#           "page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filte" \
#           "r=0&_=1534929985286".format(x)
#     res = requests.get(url).text
#     js = json.loads(res[res.index('(') + 1:-2])
#     data = js['data']['lists']
#     for i in range(10):
#         print(str(i + 1) + ">>>" + str(data[i]['FileName']).replace('<em>', '').replace('</em>', ''))
#     number = int(input("\n请输入要下载的歌曲序号（输入-1退出程序）: "))
#     if number == -1:
#         exit()
#     else:
#         name = str(data[number - 1]['FileName']).replace('<em>', '').replace('</em>', '')
#         fhash = re.findall('"FileHash":"(.*?)"', res)[number - 1]
#         hash_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash=" + fhash
#         hash_content = requests.get(hash_url)
#         play_url = ''.join(re.findall('"play_url":"(.*?)"', hash_content.text))
#         real_download_url = play_url.replace("\\", "")
#         with open(name + ".mp3", "wb")as fp:
#             fp.write(requests.get(real_download_url).content)
#         print("歌曲已下载完成！")
#
#
# if __name__ == '__main__':
#     x = input("请输入歌名：")
#     get_song(x)
# import os
# import requests
# class MusicFile(object):
#     def __init__(self,music_name):
#         k = KuGouMusicSearch(music_name) # 酷狗音乐
#         song_name,song_ext_name,file_hash = k.search_music()
#         music_file_path = os.path.join(os.path.dirname(__file__),"music")
#         self.music_file = os.path.join(music_file_path,("%s.%s"% (music_name,song_ext_name)))
#         self.url =self.find_download_url(file_hash)# 获取真正的下载url
#         if notos.path.exists(music_file_path):# 不存在目录
#             os.mkdir(music_file_path)
#             if notos.path.exists(self.music_file):# 不存在文件
#                 f =open(self.music_file,'w')
#                 f.close()
#         self.download_music_to_file()
#     def download_music_to_file(self):
#         chunk_size =1024*1024
#         result = requests.get(self.url,stream=True)
#         with open(self.music_file,"wb") as fd:
#             for chunk in result.iter_content(chunk_size=chunk_size):
#                 fd.write(chunk)
#                 @staticmethod
#     def find_download_url(file_hash):
#         url ="http://www.kugou.com/yy/index.php?r=play/getdata&hash=%s\ " %(file_hash)
#         response_json = requests.get(url).json()
#         download_url = response_json["data"]["play_url"]
#         return download_url
# class KuGouMusicSearch(object):
#     def __init__(self,music_name):
#         self.music_name = music_name
#     def search_music(self):
#         request_url ="http://songsearch.kugou.com/song_search_v2?"\"keyword=%s"\"&page=1&pagesize=30&platform=WebFilter&privilege_filter=0"% (self.music_name)
#         response_json = requests.get(request_url).json()
#         song = response_json["data"]["lists"][0]# 默认取第一个
#         song_name = song["SongName"]
#         song_ext_name = song["ExtName"]# 后缀 .mp3
#         song_file_hash = song["FileHash"]# file hash， 为下载做准备
#         returnsong_name,song_ext_name,song_file_hash
# if__name__ =='__main__':m = MusicFile("告白气球")
import requests
import json
import re

def get_song(x):
    url = "http://songsearch.kugou.com/song_search_v2?callback=jquery112407470964083509348_1534929985284&keyword={}&" \
          "page=1&pagesize=30&userid=-1&clientver=&platform=webfilter&tag=em&filter=2&iscorrection=1&privilege_filte" \
         "r=0&_=1534929985286".format(x)
    res = requests.get(url).text
    js = json.loads(res[res.index('(') + 1:-2])
    data = js['data']['lists']
    for i in range(10):
        print(str(i + 1) + ">>>" + str(data[i]['filename']).replace('<em>', '').replace('</em>', ''))
        number = int(input("\n 请输入要下载的歌曲序号（输入-1退出程序）: "))
    if number == -1:
        exit()
    else:
        name = str(data[number - 1]['filename']).replace('<em>', '').replace('</em>', '')
        fhash = re.findall('"filehash":"(.*?)"', res)[number - 1]
        hash_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash=" + fhash
        hash_content = requests.get(hash_url)
        play_url = ''.join(re.findall('"play_url":"(.*?)"', hash_content.text))
        real_download_url = play_url.replace("\\", "")
        with open(name + ".mp3", "wb")as fp:
           fp.write(requests.get(real_download_url).content)
        print("歌曲已下载完成！")

if __name__ == '__main__':
    x = input("请输入歌名：")
    get_song(x)