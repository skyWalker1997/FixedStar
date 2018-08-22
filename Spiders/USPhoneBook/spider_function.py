#coding:utf-8
import re

Name = []

Address = []
Phone  = []
Relatives = []
Associate = []

def func(content):
    pattern_Name = re.compile(u'<span itemprop="name" class="header-name">(.*?)</span>', re.S)
    pattern_Streetname = re.compile(u'Current.*?Address.*?address.*?>(.*?)</p>', re.S)
    pattern_Relatives = re.compile(u'Relatives:.*?<div.*?>(.*?)</div>',re.S)
    pattern_Relatives2 = re.compile(u'<void.*?>(.*?)</void>',re.S)
    pattern_Associates = re.compile(u'Associates.*?<div.*?>(.*?)</div>',re.S)
    pattern_Associates2 = re.compile(u'<a href=.*?<void.*?>(.*?)</void>',re.S)


    result_Name = re.findall(pattern_Name, content)
    result_Streetname = re.findall(pattern_Streetname, content)
    temp_Ralatives = re.findall(pattern_Relatives,content)
    temp_Associate = re.findall(pattern_Associates,content)



    #print "同事"
    result_Associate = re.findall(pattern_Associates2,str(temp_Associate).encode('utf-8'))
    for r_Associate in result_Associate:
        r_Associate = str(r_Associate).replace("\\n","")
        Associate.append(r_Associate)

    #print temp_Associate

    result_relatives = re.findall(pattern_Relatives2,str(temp_Ralatives).encode('utf-8'))

    for r_relatives in result_relatives:
        r_relatives = str(r_relatives).replace("\\n","")
        temp_judge  = "<span class="
        if temp_judge in r_relatives:
            r_relatives = ""
        Relatives.append(r_relatives)

    for r_Name ,r_Street in zip(result_Name,result_Streetname):
        temp_address = str(r_Street.encode('utf-8'))
        r_Name  = str(r_Name.encode('utf-8'))
        Name.append(r_Name)
        Address.append(temp_address)

    return Name,Address,Relatives,Associate