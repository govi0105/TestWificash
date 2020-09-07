import hashlib,csv,requests,time,json,threading,random
def Md5(loginName):
    m=hashlib.md5()
    data="oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgNchannelId=3|langType=en|loginName="+loginName+"|loginPwd=e10adc3949ba59abbe56e057f20f883e|mobileType=2|versionNumber=1.3.9"
    m.update(data.encode('utf-8'))
    # print(m.hexdigest())
    return m.hexdigest()
def Phone():
    phone=[]
    csv_reader = csv.reader(open('D:\city.csv','r'))
    for row in csv_reader:
        if row[0]=='手机号码':
           continue
        phone.append(row[0])
    return phone
def logon(headers,data):
    url="https://apitest.wificash.in/api/user/login.htm"
    r = requests.post(url,headers=headers,data=data)
    print(r.text)
header ={}
header["IMEI"]="863064010183111"
data = {"mobileType":"2","versionNumber":"1.3.9","loginPwd":"e10adc3949ba59abbe56e057f20f883e","channelId":"3","langType":"en"}

phone = Phone()
for loginName in phone:
    # print("手机号码：%s" %loginName)
    data["loginName"]=loginName
    # print("MD5加密：",end='')
    header["signMsg"] =Md5(loginName)
    print(header)
    print(data)
    logon(header,data)


