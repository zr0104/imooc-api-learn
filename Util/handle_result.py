#coding=utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import json
from Util.handle_json import get_value
#print(get_value("api3/getbanneradvertver2","/Config/code_message.json"))
'''[
        {"1006": "token error"},
        {"10001": "用户名错误"},
        {"10002": "密码错误"}
    ]'''

def handle_result(url,code):
    print("------>",code,"------>",type(code))
    data = get_value(url,"/Config/code_message.json")
    if data !=None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None


if __name__ == '__main__':
    print(handle_result('api3/getbanneradvertver2',"10002"))