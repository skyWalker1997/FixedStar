#coding:utf-8
import requests
import urllib
import urllib2
import re


#
#
#
# content = ""
# url = "http://www.cvedetails.com/cve/CVE-2017-8464/?q=CVE-2017-8464"
# user_agent = 'Chrome/31.0.1650.63'
# headers = {'User-Agent': user_agent}
# try:
#     request = urllib2.Request(url, headers=headers)
#     response = urllib2.urlopen(request, timeout=15)
#     content = response.read().decode('utf-8')
#     print content
# except Exception as e:
#     print e
# # #
# pattern = re.compile(u'panel panel-(.*?)".*?Website Address.*?<strong>(.*?)</strong>.*?Analysis.*?<td>(.*?)&.*?Blacklist Status.*?label-danger.*?>(.*?)</span>.*?Domain Registration.*?<td>(.*?)</td>.*?IP Address.*?<strong>(.*?)</strong>.*?Reverse DNS.*?<td>(.*?)</td>.*?ASN.*?<a.*?>(.*?)</a>.*?Server Location.*?/>(.*?)</td>.*?Longitude.*?<td>(.*?)&.*?City.*?<td>(.*?)</td>.*?Region.*?<td>(.*?)</td>',re.S)
# # pattern = re.compile(u'tabletitle.*?<nobr>(.*?)</nobr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
# # # pattern = re.compile(u'<th>Email-IP.*?ip_whois.*?>(.*?)</a>.*?<th>Streetname:.*?<td>(.*?)</td>.*?<th>Address:.*?<td>(.*?)</td>.*?<th>City:.*?<td>(.*?)</td>.*?State.*?<td>(.*?)</td>.*?Gender:.*?<td>(.*?)</td>',re.S)
# # # pattern = re.compile(u'<a href="/name/(.*?)">.*?<a href.*?/address/(.*?)">.*?<span itemprop="telephone">(.*?)</span>.*?<span itemprop="email">(.*?)</span>.*?<a href="/ip/(.*?)">',re.S)
# result = re.findall(pattern,content)
# print result
#
import socket


# import urllib3.util.ssl_
# print(urllib3.util.ssl_.DEFAULT_CIPHERS)
# urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

content = ""
from Monitor.Util.OutputColor_Util import Logger

url = "https://totalhash.cymru.com/analysis/?2be25b741214f07f2b111e88bcfac7cd5274f6e8"
try:
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=70)
    content = response.read().decode('utf-8')
    #print content
except Exception as e:
    if str(e).find("timed out") == 1:
        print e
        print Logger.FAIL + "TIME OUT" + Logger.ENDC
    else:
        print e
else:
    print content
    pattern = re.compile(u'<th>AV</th>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
    result = re.findall(pattern, content)
    print result
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
# url = "http://www.toolsvoid.com/ip-address-lookup"
# MD5 = "111.73.45.188"
#
# headers = {
#
#     "Content-Type": "application/x-www-form-urlencoded",
# }
#
# test_data = {"ipaddr": MD5}
# test_data_urlencode = urllib.urlencode(test_data)
# session = requests.session()
# requ = session.post(url, data=test_data_urlencode, headers=headers ,timeout = 15)
# print requ.content
# pattern = re.compile(u'<table.*?<strong>(.*?)</strong>.*?IP Hostname.*?<td>(.*?)</td>.*?Continent.*?<td>(.*?)</td>.*?Country Code.*?src=.*?>(.*?)</td>.*?Region.*?<td>(.*?)</td>.*?Lat.*?<td>(.*?)</td>.*?ASN.*?<td>(.*?)</td>.*?AS Owner.*?value="(.*?)".*?Internet Service Provider.*?value="(.*?)".*?ISP.*?value="(.*?)"', re.S)
# result = re.findall(pattern, requ.content)
# print result

