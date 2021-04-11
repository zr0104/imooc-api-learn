# coding=utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
import json
import requests
from Util.handle_json import get_value
from Util.handle_init import handle_ini

class BaseRequest:
    def send_post(self,url,data):
        '''
        发送post请求
        '''
        res = requests.post(url=url,data=data).text
        return res

    def send_get(self,url,data):
        '''
        发送get请求
        '''
        res = requests.get(url=url,params=data).text
        return res

    def run_main(self,method,url,data):
        '''
        执行方法，传递method、url、data参数
        '''
        #return get_value(url)
        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url + url
        #print(url)
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        try:
            res = json.loads(res)
            #print("这个结果是一个json")
        except:
            print("这个结果是一个text")
        #print("--->",res)
        return res


request = BaseRequest()
if __name__ == '__main__':
    request = BaseRequest()
    request.run_main('get','login',"{'username':'11111'}")