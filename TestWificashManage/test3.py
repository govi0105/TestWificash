'''=================================================
@Project -> File   ：TestWificash -> test3
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/9/1 10:59
@Desc   ：
=================================================='''
import logging
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"d:/TestWificash/Outputs/Logs/test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

logging.info("截图成功，文件路径为：{}".format("d:/TestWificash/Outputs/Logs/test.log" ))
try:

    a=3
    b=0
    c = a/b
except:
    logging.exception("")
    raise