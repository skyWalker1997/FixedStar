import socket
import urllib2
from Monitor.Util.OutputColor_Util import Logger


def request_infor(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request, timeout=10)
        content = response.read().decode('utf-8')
    except Exception as e:
        if str(e).find("timed out"):
            print Logger.FAIL + "TIME OUT" + Logger.ENDC
            return "",1
    else:
        return content,0