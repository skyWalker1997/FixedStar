# -*- coding: utf-8 -*-
import urllib2
import requests
import re
from collections import OrderedDict

i=0
results=[]
test_result = []
#temp_dict= OrderedDict([('Data',''),('URL',''),('MD5',''),('IP',''),('Tools','')])
for i in range(10):
    # http://vxvault.net/ViriList.php?s=40&m=40
    page = i*40
    url = 'http://vxvault.net/ViriList.php?s='+str(page)+'&m=40'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print(content)
    #content = "<a  href='ViriFiche.php?ID=38836'>07-07</a></TD>"
    dict_info = OrderedDict()
    dict_info = {'Date': '', 'URL': '', 'MD5': '', 'IP': '', 'Tools': ''}





    #pattern_All = re.compile(u'<TR>.*?ID=.*?>(.*?)</a></TD>.*?\[D\]</a>.*?>(.*?)</a></TD>.*?<a.*?MD5=.*?>(.*?)</a>.*?<a.*?IP=.*?>(.*?)</a>.*?<a.*?pedump.*?>(.*?)</a>.*?>(.*?)</a>',re.S)



    pattern_Data = re.compile(u'<TR>.*?ID=.*?>(.*?)</a>', re.S)
    pattern_URL = re.compile(u'<a.*?\[D\]</a>.*?>(.*?)</a>', re.S)
    pattern_MD5 = re.compile(u'<a.*?MD5=.*?>(.*?)</a>',re.S)
    pattern_IP = re.compile(u'<a.*?IP=.*?>(.*?)</a>',re.S)
    pattern_Tools = re.compile(u'<a.*?pedump.*?>(.*?)</a>.*?>(.*?)</a>',re.S)

    #result_all = re.findall(pattern_All,content)

    result_Data = re.findall(pattern_Data, content)
    result_URL = re.findall(pattern_URL, content)
    result_MD5 = re.findall(pattern_MD5,content)
    result_IP = re.findall(pattern_IP,content)
    result_Tools = re.findall(pattern_Tools,content)


    # print(result_all)


    # Count = len(result_Data)
    # print (Count)
    # Count = len(result_URL)
    # print (Count)
    # Count = len(result_MD5)
    # print (Count)
    # Count = len(result_IP)
    # print (Count)
    # Count = len(result_Tools)
    # print (Count)

    # for res in result_all:
    #     results.append(res)
    #
    # Data = []
    # URL = []
    # MD5 = []
    # IP = []
    # Tools = []
    #
    # for result in result_Data:
    #     dict_info['Data'] = result.encode('utf-8')
    #     Data.append(dict_info['Data'])
    # for result in result_URL:
    #     dict_info['URL'] = result.encode('utf-8')
    #     URL.append(dict_info['URL'])
    # for result in result_MD5:
    #     dict_info['MD5']  = result.encode('utf-8')
    #     MD5.append(dict_info['MD5'])
    # for result in result_IP:
    #     dict_info['IP'] = result.encode('utf-8')
    #     IP.append(dict_info['IP'])
    # for result in result_Tools:
    #     dict_info['Tools'] = result.encode('utf-8')
    #     Tools.append(dict_info['Tools'])
    #
    # for i in range(400):
    #     temp_dict['URL'] =
    #     results.append()


    for r_Date ,r_URL,r_MD5,r_IP,r_Tools in zip(result_Data,result_URL,result_MD5,result_IP,result_Tools):
        dict_info = {'Date': '', 'URL': '', 'MD5': '', 'IP': '', 'Tools': ''}
        dict_info['Date'] = r_Date.encode('utf-8')
        dict_info['URL'] = r_URL.encode('utf-8')
        dict_info['MD5'] = r_MD5.encode('utf-8')
        dict_info['IP'] = r_IP.encode('utf-8')
        dict_info['Tools'] = str(r_Tools[0].encode('utf-8'))+str(r_Tools[1].encode('utf-8'))
        test_result.append(dict_info)

    ran = len(test_result)
    for i in range(ran):
        print test_result[i]

# i = 0
# for i in range(400):
#     res_out = str(results[i]).encode('utf-8')
#
#     print(i,":",res_out)
#
#
#
# print(result_Data)
# print(result_URL)
# print(result_MD5)
# print(result_IP)
# print(result_Tools)
# #i = 0
# print("分组打印")
# for i in range(Count_Name):
#    print("Name :",dict_info['Name'][i],"Address :",dict_info['Address'][i],"Name :",dict_info['Age'][i],"Name :",dict_info['Phone'][i]
#          ,"Email :",dict_info['Email'][i],"IP :",dict_info['IP'][i])
#
#
