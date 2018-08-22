import urllib2


def request_infor(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request,timeout=60)
    content = response.read().decode('utf-8')
    return content