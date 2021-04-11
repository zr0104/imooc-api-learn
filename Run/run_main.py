#coding=utf-8
import sys
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
print(base_path)
from collections.abc import Iterable
from Util.handle_excel import excel_data
import json
from Util.handle_excel import excel_data
from Util.handle_result import handle_result
from Base.base_request import request

#['imooc_001', '登陆', 'yes', None, 'login', 'post', '{"username":"111111"}', 'yes', 'message', None]
class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                method = data[6]
                url = data[5]
                data1 = data[7]
                excepect_method = data[10]
                excepect_result = data[11]
                res = request.run_main(method,url,data1)
                code = str(res['errorCode'])
                message = res['errorDesc']
                if excepect_method == 'mec':
                    config_message = handle_result(url,code)
                    if message == config_message:
                        print("测试case通过")
                    else:
                        print("测试case失败")
                if excepect_method == 'errorCode':
                    if excepect_result == code:
                        print("测试case通过")
                    else:
                        print("测试case失败")
                if excepect_method == 'json':
                    print("没有找到执行方式")


if __name__ == '__main__':
    run = RunMain()
    run.run_case()