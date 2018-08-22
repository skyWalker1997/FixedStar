# -*- coding: utf-8 -*-
import urllib2

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.Spider  #连接mydb数据库，没有则自动创建
my_set = db.Email_Format #使用test_set集合，没有则自动创建





results=[]

print "请输入想要查找的域名"
domain_search = raw_input()
url = 'https://www.email-format.com/d/'+domain_search
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#response  = requests.get(url)
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request,timeout=60)
results =  Spiders.Email_Format.spider_function.func(response.read().encode('utf-8'))





for re in results:
    print re

#
# pattern_Email = re.compile(u"email'.*?data-id=.*?fl'>(.*?)</div>", re.S)
# result_Email = re.findall(pattern_Email, content)
#
# i = 4
# for r_Email in result_Email:
#     temp = str(r_Email.encode('utf-8').replace("\n\t\t\t\t", ''))
#     t_email = temp.strip()
#     my_set.insert({"id":i,"Email_Format-Format":t_email})
#     i=i+1
# #print Email_Format-Format

