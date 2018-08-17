#coding:utf-8
import requests
import urllib
import urllib2
import re


#
#
#
# content = ""
# url = "https://www.projecthoneypot.org/ip_103.48.36.115"
# user_agent = 'Chrome/31.0.1650.63'
# headers = {'User-Agent': user_agent}
# try:
#     request = urllib2.Request(url, headers=headers)
#     response = urllib2.urlopen(request, timeout=10)
#     content = response.read().decode('utf-8')
# except Exception as e:
#     print e
#
# pattern = re.compile(u'.*?Geographic.*?Location.*?title="(.*?)"',re.S)
#pattern = re.compile(u'<th>Email-IP.*?ip_whois.*?>(.*?)</a>.*?<th>Streetname:.*?<td>(.*?)</td>.*?<th>Address:.*?<td>(.*?)</td>.*?<th>City:.*?<td>(.*?)</td>.*?State.*?<td>(.*?)</td>.*?Gender:.*?<td>(.*?)</td>',re.S)
# pattern = re.compile(u'<a href="/name/(.*?)">.*?<a href.*?/address/(.*?)">.*?<span itemprop="telephone">(.*?)</span>.*?<span itemprop="email">(.*?)</span>.*?<a href="/ip/(.*?)">',re.S)
# result = re.findall(pattern,content)
#
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
# content = ""
# url = "http://vxvault.net/ViriList.php"
# MD5 = "C56EC45DFCCA4A3A947D6B5B1ED7F22A"
#
# headers = {
#
#     "Content-Type": "application/x-www-form-urlencoded",
# }
#
# test_data = {"MD5": MD5}
# test_data_urlencode = urllib.urlencode(test_data)
# session = requests.session()
# requ = session.post(url, data=test_data_urlencode, headers=headers)
# pattern = re.compile(u'<TR>.*?ID=.*?>(.*?)</a>.*?<a.*?\[D\]</a>.*?>(.*?)</a>.*?<a.*?php\?MD5=.*?>(.*?)</a>.*?<a.*?IP=.*?>(.*?)</a>.*?<a.*?pedump.*?>(.*?)</a>.*?>(.*?)</a>', re.S)
# result = re.findall(pattern, requ.content)
# print result
url = "http://www.ipvoid.com/ip-geolocation/"
MD5 = "69.195.129.70"

headers = {

    "Content-Type": "application/x-www-form-urlencoded",
}

test_data = {"ip": MD5}
test_data_urlencode = urllib.urlencode(test_data)
session = requests.session()
requ = session.post(url, data=test_data_urlencode, headers=headers ,timeout = 15)
print requ.content
pattern = re.compile(u'IP.*?Address:(.*?)Hostname:(.*?).*?Organization:(.*?)ASN:(.*?)Continent:(.*?)Country:(.*?)Latitude.*?Longitude:(.*?)Region:(.*?)City:(.*?)<', re.S)
result = re.findall(pattern, requ.content)
print result

