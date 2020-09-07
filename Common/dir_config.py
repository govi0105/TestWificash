'''=================================================
@Project -> File   ：TestWificash -> dir_config
@IDE    ：PyCharm
@Author ：高伟
@Date   ：2020/8/27 16:32
@Desc   ：
=================================================='''
import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__ ))[0])[0]
testdatas_dir=os.path.join(base_dir,"TestDatas")
testcases_dir=os.path.join(base_dir,"TestWificashManage")
htmlreport_dir=os.path.join(base_dir,"Outputs/Reports")
logs_dir=os.path.join(base_dir,"Outputs/Logs")
# config.dir=os.path.join(base dir,"Config")
screenshot_dir=os.path.join(base_dir,"Outputs/Screenshots")