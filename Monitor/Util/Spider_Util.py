#coding:utf-8
import re
import Request_Util



def Consult(site):
    if cmp(str(site.RequstType).encode('utf-8'),"GET") == 0:
        site.SiteUrl = str(site.SiteUrl).encode('utf-8') + str(site.ExampleInPut).encode('utf-8')
        content,TimeOutFlag = Request_Util.get_request_infor(site)
        if TimeOutFlag == 0:
            pattern = re.compile(u''+site.Regex,re.S)
            result = re.findall(pattern,str(content))

            print result
            return result
        else:
            return ""
    elif cmp(str(site.RequstType).encode('utf-8'),"POST") == 0:
        site.SiteUrl = str(site.SiteUrl).encode('utf-8') + str(site.ExampleInPut).encode('utf-8')
        content, TimeOutFlag = Request_Util.post_request_info(site)
        if TimeOutFlag == 0:
            pattern = re.compile(u''+site.Regex,re.S)
            result = re.findall(pattern,str(content))
            print result
            return result
        else:
            return ""
    else:
        site.SiteUrl = str(site.SiteUrl).encode('utf-8') + str(site.ExampleInPut).encode('utf-8')
        content, TimeOutFlag = Request_Util.get_request_infor(site)
        if TimeOutFlag == 0:
            result = str(content)
            print result
            return result
        else:
            return ""
