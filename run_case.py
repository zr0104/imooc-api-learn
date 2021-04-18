#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from Base.send_email import send_email

# 获取当前py文件的绝对路径
base_path1 = os.path.dirname(os.path.realpath(__file__))
print(base_path1)

# 1: 加载测试用例
def all_test():
    case_path = os.path.join(base_path1, "Run")
    suite = unittest.TestLoader().discover(start_dir=case_path, pattern="test_*.py", top_level_dir=None)
    return suite


# 2:执行测试用例
def run():
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    #  测试报告路径
    file_name = os.path.join(base_path1, "Report") + "/" + now + "report.html"
    with open(file_name, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="Sen接口自动化测试报告", description="环境：window 10 浏览器：chrome")
        runner.run(all_test())
    f.close()


# 3:获取最新的测试报告
def get_report(report_path):
    list = os.listdir(report_path)
    list.sort(key=lambda x: os.path.getmtime(os.path.join(report_path, x)))
    print("测试报告：", list[-1])
    report_file = os.path.join(report_path, list[-1])
    return report_file


# # 4:发送邮件
# def send_mail(subject, report_file, file_name):
#     #  读取测试报告内容，作为邮件的正文内容
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     send_mail(subject, mail_body, file_name)

def get_email_body(report_file):
    #  读取测试报告内容，作为邮件的正文内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    return mail_body


if __name__ == "__main__":
    run()
    report_path = os.path.join(base_path1, "Report")  # 测试报告路径
    report_file = get_report(report_path)  # 测试报告文件
    email_body = get_email_body(report_file)
    subject = "Sen-imooc接口测试报告"  # 邮件主题
    file_names = [report_file]  # 邮件附件
    # 发送邮件
    send_email(subject, email_body, file_names)
