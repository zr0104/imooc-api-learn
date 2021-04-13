#coding=utf-8
import sys
import os
sys.path.append("../")
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
from Util.handle_json import read_json
import hashlib

def get_header():
    data = read_json("/Config/header.json")
    # print(data)
    return data

def header_md5():
    '''
    header某个字段的md5格式转换
    '''
    #key = '123456478999dddddd'
    data = get_header()
    key = data['imooc_key']
    b = key.encode(encoding='utf-8')
    #创建md5对象
    m = hashlib.md5()
    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    m.update(b)
    data_md5 = m.hexdigest()
    print('MD5加密前前：' +key)
    print('MD5加密前后：' +data_md5)
    return data_md5

# if __name__ == '__main__':
#     header_md5()
