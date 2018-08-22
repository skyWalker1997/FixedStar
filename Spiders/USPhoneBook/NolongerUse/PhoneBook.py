# -*- coding: utf-8 -*-
import urllib2
from pymongo import MongoClient
import Spiders.USPhoneBook.spider_function
# conn = MongoClient('localhost', 27017)
# db = conn.Spider  #连接mydb数据库，没有则自动创建
# my_set = db.PhoneBook #使用test_set集合，没有则自动创建
#


import Spiders.USPhoneBook.spider_function
i=0
results=[]
test_result = []
#temp_dict= OrderedDict([('Data',''),('URL',''),('MD5',''),('IP',''),('Tools','')])

# http://vxvault.net/ViriList.php?s=40&m=40
url = 'https://www.usphonebook.com/863-424-7777/detailed'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
#print(content)
#content = "Associates:</p><div class=\"ls_contacts-block ls_contacts-group ls_contacts-group-columns\"><p class=\"full-map-wrapper-desc\"><a href='/cornal-chappin/G-4246806282196777905' class=\"ls_success-blue-link\">Cornal Chappin</a></p></div>"

Name,Address,Relatives,Associate = Spiders.USPhoneBook.spider_function.func(content)
print Name,Address,Relatives,Associate
#
# i = 0
# for t_Name,t_Address,t_Relatives,t_Associate in zip(Name,Address,Relatives,Associate):
#     my_set.insert({"_id": i,"Name":str(t_Name),"Address": str(t_Address),"Relatives":Relatives,"Associate":Associate})
#
