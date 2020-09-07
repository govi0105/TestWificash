import hashlib
class MD5():
    data = 'oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgN'
    keys = ''
    def __int__(self,token='',userId='',loginName=''):
        self.token = token
        self.userId=userId
        self.loginName=loginName
        list = ['mobileType=2', 'langType=en', 'userId='+self.userId,"loginName="+self.loginName,"loginPwd=e10adc3949ba59abbe56e057f20f883e",'versionNumber=1.3.9', 'channelId=3']
        if userId=='':
            list.remove('userId='+self.userId)
            if loginName=='':
                list.remove("loginName="+self.loginName)
                list.remove("loginPwd=e10adc3949ba59abbe56e057f20f883e")
        # data = 'oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgN'
        global key
        # keys=''
        list.sort()
        for i in range(len(list)):
            if i < len(list) - 1:
                self.keys += list[i] + "|"
            else:
                self.keys += list[i]
        key = self.data + self.token + self.keys

        print(list)
        print(key)

if __name__=='__main__':
    toke='1aa138eedfed4e8dbe6c582042191264'
    # userId = '921'
    test=MD5().__int__(token=toke)

# ['channelId=3', 'langType=en', 'mobileType=2', 'userId=921', 'versionNumber=1.3.9']
# oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgN1aa138eedfed4e8dbe6c582042191264channelId=3|langType=en|mobileType=2|userId=921|versionNumber=1.3.9
# 45196ba6223972c6f093f661e84088aa
# import hashlib,csv,requests,time,json,threading,random
def Md5():
    m=hashlib.md5()
    m.update(key.encode('utf-8'))
    return  m.hexdigest()
print(Md5())
