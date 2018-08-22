import requests
import socket
import urllib
import urllib2
from OutputColor_Util import Logger



def get_request_infor(site):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(site.SiteUrl, headers=headers)
        timeout = int(str(site.TimeOut).encode('utf-8'))
        response = urllib2.urlopen(request, timeout=timeout)
        content = response.read().decode('utf-8')
    except Exception as e:
        if str(e).find("timed out"):
            print Logger.FAIL + "TIME OUT" + Logger.ENDC
            return "",1
        else:
            print e
    else:
        return content,0
def post_request_info(site):
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        test_data = {str(site.ExampleInPutType).encode('utf-8'):str(site.ExampleInPut).encode('utf-8')}
        test_data_urlencode = urllib.urlencode(test_data)
        session = requests.session()
        requ = session.post(site.SiteUrl, data=test_data_urlencode, headers=headers, timeout=int(str(site.TimeOut).encode('utf-8')))
        content = requ.content
        return content, 0
    except Exception as e:
        if str(e).find("timed out"):
            print Logger.FAIL + "TIME OUT" + Logger.ENDC
            return "",1
        else:
            print e

