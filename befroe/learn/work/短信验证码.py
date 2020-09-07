import re
import pymysql
st = '6319 is your Getmoney verification code and 1 minute valid,Please complete the verification as soon as possible.'
li=re.findall(r"\d",st)
print(li)
for i in range(len(li)) :
    li[i]=int(li[i])
print(li)
del li[-1]
print(li)
# li.pop()
# print(li)
db = pymysql.connect("global-mobile-hujin-zhu.mysql.database.azure.com","qqyd_hujin@global-mobile-hujin-zhu","MUUC#QuuKBUs","global-mobile-hujin-zhu.mysql.database.azure.com",charset = 'utf8')
# user = 'qqyd_hujin@global-mobile-hujin-zhu'
# pwd  = 'MUUC#QuuKBUs'
# host = 'global-mobile-hujin-zhu.mysql.database.azure.com'
# db   = 'test'
# data_file = 'in_superloan_uat.dat'
# select_sql = "select msg_text from message_send_record where phone_number='1000000001'"
# print(select_sql)