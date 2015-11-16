# coding: utf-8
import os
import os.path
import codecs
import json


class test_cl(object):
    exposed = True    
        
    def __init__(self):
        pass
    
    def NEGER(self):        
        in_file = open("data.json","r")
        new_dict = json.load(in_file)
        in_file.close()
        
        return json.dumps(new_dict)
    
    def POST(self, **data_s):
        print(data_s)