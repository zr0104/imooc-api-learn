# coding=utf-8
import json
import requests

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
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
            try:
                res = json.loads(res)
            except:
                print("这个结果是一个text")
        return res

request = BaseRequest()
