import requests,time,json,threading,random
def logon(headers,data):
    url="https://apitest.wificash.in/api/user/login.htm"
    global errow
    errow = 0
    try:
        r = requests.post(url, headers=headers, data=data)
        if r.json().get('code') != 0:
            print(r.json())
            errow += 1
    except Exception as e:
        print(e)
        errow += 1
    # print(r.json().get('data').get('token'))
    print(r.text)
    print(errow)
    print(r.headers.get('Content-Type'))
def testonework(headers,data):
    '''一次并发处理单个任务'''
    i = 0
    while i < user_number:
        i += 1
        logon(headers,data)
    time.sleep(think_tome)

def run(n,headers,data):
    '''使用多线程进程并发测试'''
    t1 = time.time()
    Threads = []
    for i in range(n):
        t = threading.Thread(target=testonework(headers,data), name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)
        print("T" + str(i))
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
    t2 = time.time()
    print("===============压测结果===================")
    print("任务数量:=", 1 * n*user_number)

    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (1 * n*user_number))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (1 * n*user_number)))
    print("错误数量:",errow )
headers={"IMEI": "863064010183111", "signMsg":"04a95c8efd3b6dd715958828d45cb4d1"}
data={"mobileType":"2","versionNumber":"1.3.9", "loginPwd":"e10adc3949ba59abbe56e057f20f883e","channelId": "3","loginName":"1230000095","langType":"en"}
# logon(headers,data)
n=3
user_number=5
think_tome = 0.5
run(n,headers,data)

# import requests,time,json,threading,random
#
# class Presstest(object):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'Content-Type': 'application/json; charset=UTF-8'}
#     def __init__(self,login_url,press_url,phone="1376193000",password="123456"):
#         self.login_url = login_url
#         self.press_url = press_url
#         self.phone = phone
#
#         self.password = password
#         self.session = requests.Session()
#         self.session.headers = self.headers
#     def login(self):
#         '''登陆获取session'''
#         data = {'t': int(time.time() * 1000), 'userName': self.phone, 'passWord': self.password}
#         res = self.session.post(self.login_url,data=json.dumps(data))
#         XToken = res.json().get('data').get('companyToken')
#         self.session.headers['X-Token'] = XToken
#         print(XToken)
# if __name__=='__main__':
#     login_url = 'https://ds.xxxxx.com/sys/sysUser/login'
#     press_url = 'https://ds.xxxxx.com/weshop/order/checkout'
#     phone = "1376193000"
#     password = "123456"
#     obj = Presstest(login_url=login_url, press_url=press_url, phone=phone, password=password)
#     obj.login()