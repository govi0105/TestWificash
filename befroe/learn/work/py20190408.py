# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise OSError('uncooperative user')
#         print(complaint)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# d_c ={"name":"xcxx","sex":"male","hobby":"male"}
# a = d_c["hobby"]
# print(a)
# d_c["hobby"]="beautiful"
# print(d_c)
for i in range(1):
    bj1 = 400*0.5
    bj2 = bj1*0.3
    bj3 = bj1*0.2
    x1 = float(input("邀请用户："))
    y1 = float(input("注册通过用户："))
    a1 = x1*10
    b1 = bj1*y1
    p1 = a1 + b1
    x2 = float(input("二级邀请用户："))
    y2 = float(input("二级注册通过用户："))
    a2 = x2*0
    b2 =bj2*y2
    p2 = a2+b2
    x3 = float(input("三级邀请用户："))
    y3 = float(input("三级注册通过用户："))
    a3 = x3 * 0
    b3 = bj3 * y3
    p3 = a3 + b3
    p= p1+p2+p3
print(p)