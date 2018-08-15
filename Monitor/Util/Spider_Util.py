import re

from Monitor.Util import Request_Util
from Monitor import Site


def Consult(site):

    if cmp(str(site.RequstType).encode('utf-8'),"GET") != -1:
        Url = str(site.SiteUrl).encode('utf-8') + str(site.ExampleInPut).encode('utf-8')
        content,TimeOutFlag = Request_Util.get_request_infor(Url)
        if TimeOutFlag == 0:
            pattern = re.compile(u''+site.Regex,re.S)
            result = re.findall(pattern,content)
            print result
            return result
        else:
            return ""
    else:
        content, TimeOutFlag = Request_Util.post_request_info(site)
        if TimeOutFlag == 0:
            pattern = re.compile(u''+site.Regex,re.S)
            result = re.findall(pattern,content)
            print result
            return result
        else:
            return ""