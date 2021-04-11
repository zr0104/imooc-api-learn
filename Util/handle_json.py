#coding=utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
#print(base_path)
import json
#from jsonpath_rw import jsonpath,parse

def read_json(file_name=None):
    if file_name == None:
        file_path = base_path+"/Config/user_data.json"
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='utf-8') as f:
        data = json.load(f)
        return data

def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)
    #return data[key]