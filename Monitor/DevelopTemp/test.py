import urllib2
import re
#
content = ""
url = "https://www.usphonebook.com/863-424-7777/detailed"
user_agent = 'Chrome/31.0.1650.63'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=10)
    content = response.read().decode('utf-8')
except Exception as e:
    print e

print content
#pattern = re.compile(u'<th>Email-IP.*?ip_whois.*?>(.*?)</a>.*?<th>Streetname:.*?<td>(.*?)</td>.*?<th>Address:.*?<td>(.*?)</td>.*?<th>City:.*?<td>(.*?)</td>.*?State.*?<td>(.*?)</td>.*?Gender:.*?<td>(.*?)</td>',re.S)
# pattern = re.compile(u'<a href="/name/(.*?)">.*?<a href.*?/address/(.*?)">.*?<span itemprop="telephone">(.*?)</span>.*?<span itemprop="email">(.*?)</span>.*?<a href="/ip/(.*?)">',re.S)
# result = re.findall(pattern,content)
# print result
#
import socket
# import urllib2
# #
# # content = ""
# # from Monitor.Util.OutputColor_Util import Logger
# #
# # url = "https://www.email-format.com/d/bjtu.edu.cn"
# # try:
# #     user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# #     headers = {'User-Agent': user_agent}
# #     request = urllib2.Request(url, headers=headers)
# #     response = urllib2.urlopen(request, timeout=10)
# #     content = response.read().decode('utf-8')
# # except Exception as e:
# #     if str(e).find("timed out"):
# #         print Logger.FAIL + "TIME OUT" + Logger.ENDC
# # else:
# #     print content
from py import xml

