import requests
import socket
import urllib
import urllib2
from Monitor.Util.OutputColor_Util import Logger


def get_request_infor(url):
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
            print e
    else:
        return content,0
def post_request_info(site):
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
    }
    try:
        test_data = {str(site.ExampleInPutType).encode('utf-8'):site.ExampleInPut}
        test_data_urlencode = urllib.urlencode(test_data)
        session = requests.session()
        requ = session.post(site.SiteUrl, data=test_data_urlencode, headers=headers)
        content = requ.text
    except Exception as e:
        if str(e).find("timed out"):
            print Logger.FAIL + "TIME OUT" + Logger.ENDC
            return "",1
        else:
            print e
    return requ.text,0
