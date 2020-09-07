# for i in range(1):
#     bj = 400*0.5 #初始注册通过分成
#     bj2 = bj*0.3 #二级注册通过分成
#     bj3 = bj*0.2 #三级注册通过分成
#     x1 = float(input("邀请用户："))
#     y1 = float(input("注册通过用户："))
#     a1 = x1*10
#     b1 = bj*y1
#     x2 = float(input("二级邀请用户："))
#     y2 = float(input("二级注册通过用户："))
#     a2 = x2*10
#     b2 =bj2*y2
#     x3 = float(input("三级邀请用户："))
#     y3 = float(input("三级注册通过用户："))
#     a3 = x3 * 10
#     b3 = bj3 * y3
#     user1 = a1 + b1 + b2 +b3
#
# print("初级用户：",user1)
pc = input('请输入系统 win or mac：')
def stop_appium(post_num=4723):
    '''关闭appium服务'''
    if pc.upper() =='WIN':
        p = os.popen(f'netstat  -aon|findstr {post_num}')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
            print('appium server已结束')
    elif pc.upper() == 'MAC':
        p = os.popen(f'lsof -i tcp:{post_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            print('appium server已结束')

def start_appium(post_num=4723):
    '''开启appium服务'''
    stop_appium(post_num)    # 先判断端口是否被占用，如果被占用则关闭该端口号
    # 根据系统，启动对应的服务
    cmd_dict = {
        'WIN':f' start /b appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone ',
        'MAC':f'appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone  & '
    }
    os.system(cmd_dict[pc.upper()])
    time.sleep(3)  # 等待启动完成
    print('appium启动成功')