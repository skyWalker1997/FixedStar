# -*- coding: utf-8 -*-
import urllib2

from Spiders.ReverseEgenie import spider_function

# conn = MongoClient('localhost', 27017)
# db = conn.Spider  #连接mydb数据库，没有则自动创建
# my_set = db.Reversegenie #使用test_set集合，没有则自动创建
#

print "请输入你想要查询的邮箱"
#Email_Search = raw_input()
Email_Search = "twomasplusone@aol.com"
url = 'http://www.reversegenie.com/email_search/' + Email_Search
user_agent = 'Chrome/31.0.1650.63'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request, timeout=60)
content = response.read().decode('utf-8')



Phone,Address,Gender,IP = spider_function.func(content)
print Phone ,Address,Gender,IP
# i = 0
# for t_Phone,t_Address,t_Gender,t_IP in zip(Phone,Address,Gender,IP):
#     my_set.insert({"_id": i,"Email":Email_Search,"IP": str(t_IP),"Gender":t_Gender,"Address":t_Address})
#     i = i+1
# print Phone,'\n',Address,'\n',Gender,'\n',IP