# -*- coding: utf-8 -*-
import urllib3
import requests
import re
from collections import OrderedDict
test_result = []
def MD5_func(content):
    content = content.encode('utf-8')

    Date = []
    URL = []
    MD5 = []
    IP = []
    Tools = []
    pattern_Data = re.compile(u'<TR>.*?ID=.*?>(.*?)</a>', re.S)
    pattern_URL = re.compile(u'<a.*?\[D\]</a>.*?>(.*?)</a>', re.S)
    pattern_MD5 = re.compile(u'<a.*?php\?MD5=.*?>(.*?)</a>', re.S)
    pattern_IP = re.compile(u'<a.*?IP=.*?>(.*?)</a>', re.S)
    pattern_Tools = re.compile(u'<a.*?pedump.*?>(.*?)</a>.*?>(.*?)</a>', re.S)

    result_Data = re.findall(pattern_Data, content)
    result_URL = re.findall(pattern_URL, content)
    result_MD5 = re.findall(pattern_MD5,content)
    result_IP = re.findall(pattern_IP,content)
    result_Tools = re.findall(pattern_Tools,content)



    for r_Date ,r_URL,r_MD5,r_IP,r_Tools in zip(result_Data,result_URL,result_MD5,result_IP,result_Tools):
        Date.append(r_Date.encode('utf-8'))
        URL.append(r_URL.encode('utf-8'))
        MD5.append(r_MD5.encode('utf-8'))
        IP.append(r_IP.encode('utf-8'))
        Tools.append(str(r_Tools[0].encode('utf-8'))+str(r_Tools[1].encode('utf-8')))
    return  Date,URL,MD5,IP,Tools
