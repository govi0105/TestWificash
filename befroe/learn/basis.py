# # def ask_ok(prompt, retries=4, reminder='Please try again!'):
# #     while True:
# #         ok = input(prompt)
# #         if ok in ('y', 'ye', 'yes'):
# #             return True
# #         if ok in ('n', 'no', 'nop', 'nope'):
# #             return False
# #         retries = retries - 1
# #         if retries < 0:
# #             raise ValueError('invalid user response')
# #         print(reminder)
# # class Complex:
# #     def __init__(self,realpart,imapart):
# #         self.r,self.i=realpart,imapart
# # x=Complex(3.0,5.6)
# # print(x.r,x.i)
# # while True:
# #     try:
# #        x = int(input("Please enter a number: "))
# #        break
# #     except ValueError:
# #         print("Oops!  That was no valid number.  Try again...")
#
#
# # import requests
# # r=requests
# # print(dir(requests))
#
#
# # # 登录次数
# # def ask_ok(prompt, retries=4, reminder='Please try again!'):
# #     while True:
# #         ok = input(prompt)
# #         if ok in ('y', 'ye', 'yes'):
# #             return True
# #         if ok in ('n', 'no', 'nop', 'nope'):
# #             return False
# #         retries = retries - 1
# #         if retries < 0:
# #             raise ValueError('invalid user response')
# #         print(reminder)
# #
# # ask_ok('请输入用户名：',5)
#
# # f = open('html.html','r')
# # read(f)
#
# # from datetime import date
# # now = date.today()
# # print(now)
# # nows=now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# # print(nows)
# # birthday = date(2006,5,6)
# # age = now - birthday
# # print(age.days)
# # print(age)
#
# #
# # import unittest
# # def average(values):
# #     """Computes the arithmetic mean of a list of numbers.
# #
# #     >>> print(average([20, 30, 70]))
# #     40.0
# #     """
# #     return sum(values) / len(values)
# #
# # class TestStatisticalFunctions(unittest.TestCase):
# #
# #     def test_average(self):
# #         self.assertEqual(average([20, 30, 70]), 40.0)
# #         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
# #         with self.assertRaises(ZeroDivisionError):
# #             average([])
# #         with self.assertRaises(TypeError):
# #             average(20, 30, 70)
# #
# # unittest.main()  # Calling from the command line invokes all tests
#
#
# # from timeit import Timer
# # timer1=Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# # print(timer1)
#
# # import reprlib
# # r=reprlib.repr(set('supercalifragilisticexpialidocious'))
# # print(r)
# # print(set('supercalifragilisticexpialidocious'))
#
# # import textwrap
# # doc = """The wrap() method is just like fill() except that it returns
# # a list of strings instead of one big string with newlines to separate
# # he wrapped lines."""
# # print(textwrap.fill(doc, width=40))
#
#
# import requests
# import hashlib
# def ligon(sign):
#     formdata = {
#         "mobileType": "2",
#         "versionNumber": "1.3.8",
#         "channelId": "3",
#         "loginName": "1230000095",
#         "loginPwd": "e10adc3949ba59abbe56e057f20f883e",
#
#     }
#     url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
#
#     headers = {"signMsg":"sign"," ":""}
#
#     response = requests.post(url, data=formdata, headers=headers)
#     print(response)
#     keys = formdata.sort()
#     print(keys)
#     result=''
#     # for p in len(keys):
#     #     if p>0:
#     #         result+="|"
#     #     else:
#     #         result +=((keys[p]+"="+requests.data[keys[p]]))
#     # token = requests.headers.token if requests.headers.token == ""  else ""
#     # app_key = 'oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgN'
#     # sign = hashlib.md5(app_key+token+result).toString()
# ligon(645)
#
formdata = {
    "mobileType": "2",
    "versionNumber": "1.3.8",
    "channelId": "3",
    "loginName": "1230000095",
    "loginPwd": "e10adc3949ba59abbe56e057f20f883e"
    }
result = ""
print(formdata)
for p in range(len(formdata)):
     if(p>0):
        result += "|"
print(result)
      # result += (keys[p]+"="+request.data[keys[p]])
