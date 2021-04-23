#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
#print(base_path)
from collections.abc import Iterable
from Util.handle_excel import excel_data
import ddt
import json
import unittest
from Util.handle_excel import excel_data
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Base.base_request import request
from Util.handle_cookie import write_cookie,get_cookie_value
from Util.handle_header import get_header
from Util.codition_data import get_data
from Base.logger import MyLogging
import HTMLTestRunner
data = excel_data.get_excel_data()

@ddt.ddt
class TestCaseDdt(unittest.TestCase):

    @ddt.data(*data)
    def test_main_case(self,data):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            is_run = data[2]
            case_id = data[0]
            case_name = data[1]
            log = MyLogging().logger
            i = excel_data.get_rows_number(case_id)
            if is_run == 'yes':
                log.info("【开始执行测试用例：{}】".format(case_name))
                is_depend = data[3]
                data1 = json.loads(data[7])
                log.info("请求的参数：%s" % data1)
                try:
                    if is_depend:
                        '''
                        获取依赖数据(前置条件)
                        '''
                        depend_key = data[4]    #需要更新的依赖key_id
                        depend_data = get_data(is_depend)    #依赖前置分出res_data和rule_data
                        data1[depend_key] = depend_data

                    method = data[6]
                    url = data[5]
                    is_header = data[9]
                    excepect_method = data[10]
                    excepect_result = data[11]
                    cookie_method =data[8]
                    log.info("请求的url：%s" % url)
                    if cookie_method == 'yes':
                        cookie = get_cookie_value('app')
                    if cookie_method == 'write':
                        '''
                        必须是获取到cookie
                        '''
                        get_cookie={"is_cookie":"app"}
                    if is_header == 'yes':
                        header = get_header()
                    res = request.run_main(method,url,data1,cookie,get_cookie,header)
                    log.info("返回结果：%s" % res)
                    #print(res)
                    code = str(res['code'])
                    #print(code)
                    #print(code)
                    message = res['msg']
                    if excepect_method == 'msg':
                        config_message = handle_result(url,code)
                        '''
                        if message == config_message:
                            excel_data.excel_write_data(i+2,13,"通过")
                            excel_data.excel_write_data(i+2,14, json.dumps(res))
                        else:
                            excel_data.excel_write_data(i+2,13,"失败")
                            excel_data.excel_write_data(i+2,14,json.dumps(res))
                        '''
                        try:
                            self.assertEqual(config_message,message)
                            log.info("检查点数据{}：{},返回数据：{}".format(i, message, config_message))
                            excel_data.excel_write_data(i,13,"通过")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                        except Exception as e:
                            log.info("检查点数据{}：{},返回数据：{}".format(i, message, config_message))
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                            raise e


                    if excepect_method == 'code':
                        '''
                        if excepect_result == code:
                            excel_data.excel_write_data(i+2,13,"通过")
                            excel_data.excel_write_data(i+2,14, json.dumps(res))
                        else:
                            excel_data.excel_write_data(i+2,13, "失败")
                            excel_data.excel_write_data(i+2,14, json.dumps(res))
                        '''
                        try:
                            self.assertEqual(excepect_result,code)
                            log.info("检查点数据{}：{},返回数据：{}".format(i, excepect_result, code))
                            excel_data.excel_write_data(i,13,"通过")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                        except Exception as e:
                            log.info("检查点数据{}：{},返回数据：{}".format(i, excepect_result, code))
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                            raise e

                    if excepect_method == 'json':
                        if code == 0:
                            status_str='sucess'
                        else:
                            status_str='error'
                        excepect_result = get_result_json(url,status_str)
                        result = handle_result_json(res,excepect_result)
                        '''
                        if result:
                            excel_data.excel_write_data(i+2,13,"通过")
                            excel_data.excel_write_data(i+2,14, json.dumps(res))
                        else:
                            excel_data.excel_write_data(i+2,13, "失败")
                            excel_data.excel_write_data(i+2,14, json.dumps(res))
                        '''
                        try:
                            self.assertTrue(result)
                            log.info("检查点数据:实际结果&预期结果{}：".format(result))
                            excel_data.excel_write_data(i,13,"通过")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                        except Exception as e:
                            log.info("检查点数据:实际结果&预期结果{}：".format(result))
                            excel_data.excel_write_data(i,13,"失败")
                            excel_data.excel_write_data(i,14,json.dumps(res))
                            raise e

                except Exception as e:
                    excel_data.excel_write_data(i,13,"失败")
                    # excel_data.excel_write_data(i,14,json.dumps(res))
                    raise e


if __name__ == '__main__':
    run = TestCaseDdt()
    run.test_main_case(data)
    # case_path = base_path+"/Run"
    # report_path = base_path+"/Report/run_case_ddt_report.html"
    # discover = unittest.defaultTestLoader.discover(case_path,pattern="run_case_*.py")
    # #unittest.TextTestRunner().run(discover)
    # with open(report_path,"wb") as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="sen接口自动化测试报告",description="senzrp")
    #     runner.run(discover)
    # f.close()
