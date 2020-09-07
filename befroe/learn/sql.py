import pymysql
class Utility:
    #构造方法（实例化时初始化调用的方法）
    def __init__(self):
        #连接数据库：连接函数connect（ 域名地址，用户名，密码，表文件名，编码）
        self.db = pymysql.connect('global-mobile-hujin-zhu.mysql.database.azure.com', 'qqyd_hujin@global-mobile-hujin-zhu', 'MUUC#QuuKBUs', 'indialoan_preview_wificash', charset='utf8')
        self.cursor = self.db.cursor()
    def query_one(self,sql):
        #查询一条数据
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result
    def query_all(self,sql):
        # 查询所有数据
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    def update_data(self,sql):
        #更新数据
        self.cursor.execute(sql)
        self.db.commit()
    # 析构方法
    def __del__(self):
        self.cursor.close()
        self.db.close()
        print('数据库连接已断开，清理工作完成...')


if __name__=='__main__':
    u = Utility()
    # print(u.query_all("select * from cl_user_auth where user_id =951"))
    print(u.query_all("select * from cl_sms where phone='1230000030'"))
    # print(u.query_all("select * from coupon_account_info where user_id = 358"))
    # print(u.query_one(" select a.id,a.user_id,a.user_login_name,a.coupon_id,a.coupon_name,a.recieve_count,a.remark,a.create_time,a.expired_time,a.status,b.coupon_money,b.coupon_status,b.use_condition_money,b.useful_begDate,b.useful_endDate,b.type,b.effective_day from coupon_account_info a left JOIN coupon_info b on a.coupon_id=b.id WHERE a.user_id = 358 and a.id = 2686"))

