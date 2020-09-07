# import requests
# url='https://fx.cp2y.com/data/issue_number!.jsp?ajax=truemode=1&lid=10002&target=10002&show=30&page=1&week=0'
# header={'Content-Type':'application/x-www-form-urlencoded'}
#
# def cli(url,header):
#     r=requests.get(url,header)
#
#     print(r.text)
# cli(url,header)
import random,numpy,csv,pymysql
# #以序列seq中值出现的概率来随机生成某个值
# def rand_pick(seq , probabilities):
#     x = random.uniform(0 ,1)
#     cumprob = 0.0
#     for item, item_pro in zip(seq , probabilities):
#         cumprob += item_pro
#         if x < cumprob:
#             break
#     return item
# value_list = [0 , 1]
# probabilities = [0.4 , 0.6]
# print(rand_pick(value_list, probabilities))


# for i in range(5):
#     numpy.random.seed(0)
#     p = numpy.array([0.1, 0.1, 0.4, 0.4])
#     index = numpy.random.choice([0, 1, 2, 3], p = p.ravel())
#     print(p)
i=0
num=5
list=[]
a=0.029411765
b=0.055555556
c1=0.024343682
c2=0.023221529
c3= 0.021292299
c4= 0.018538454
c5=0.015830205
c6=0.01449459
c7=0.0131769
c8=0.012979
c9=0.01289
c10=0.0099
pro=[a,a,b,a,a,c10,(c2+c3+c4)/3,b,b,c9,c5,a,a,a,a,a,a,a,(c7+c8)/2,b,a,(c2+c3+c4)/3,(c2+c3+c4)/3,a,c6,a,a,(c7+c8)/2,a,c1,b,b,a]
numbers=[]
while i<num:
    list_red = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
    list_b = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
    pro1=[0.1,0.05,0.05,0.1,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1]
    p=numpy.random.choice(list_red, 6,p=pro)
    p1=numpy.random.choice(list_b, 1,p=pro1)
    list = p
    list1=p1
    numbers = sorted(list, reverse=False)
    numbers1 = sorted(list1, reverse=False)
    if numbers[0]!=numbers[1]!=numbers[2]!=numbers[3]!=numbers[4]!=numbers[5]:
        # print(numbers)
        # print(numbers1)
        lottery=numbers+numbers1
        print(lottery)
        db = pymysql.connect('localhost', 'root', '123456', 'loan', charset='utf8')
        cursor = db.cursor()

        # sql = "INSERT INTO activity_data(id,date,math_data,rmark) VALUES(%s, %s,%s,%s')"%('null','null',lottery,'null')
        sql = "INSERT INTO activity_data(id,date,math_data,rmark) VALUES(null, null,'1','1')"
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        print(result)
        # with open('D:\\360Downloads\\ew.csv','a',) as csvfile:
        #     # 定义一个写变量
        #     # writeCSV = csv.writer(csvfile)
        #     # writeCSV.writerow(lottery)
        #     writer = csv.writer(csvfile, dialect='excel', lineterminator='\n')
        #     writer.writerow(lottery)

        i += 1