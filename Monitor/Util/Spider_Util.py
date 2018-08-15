import re

from Monitor.Util import Request_Util
from Monitor import Site


def Consult(site):
    Url = str(site.SiteUrl).encode('utf-8')+str(site.ExampleInPut).encode('utf-8')
    content,TimeOutFlag = Request_Util.request_infor(Url)
    if TimeOutFlag == 0:
        pattern = re.compile(u''+site.Regex,re.S)
        result = re.findall(pattern,content)
        return result
    else:
        return ""