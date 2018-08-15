#coding:utf-8

import DB_util
import Request_util
from Spiders.ReverseEgenie import spider_function


def main():

    """数据库信息"""
    portnumb = 27017
    hostname = "localhost"
    DataBaseName  = "Spider"
    CollectionName = "Reversegenie"


    """存储字段定义"""


    """报文构造"""
    print "请输入你想查询的邮箱"
    Email_Search = raw_input()

    """数据库连接"""
    conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)

    """搜索数据库中是否已有相关记录"""
    find = DB_util.MongoDBfindifExists(conn, Email_Search)
    if(find != None):
        print "Mongofind:"
    else:
        url = 'http://www.reversegenie.com/email_search/' + Email_Search
        content = Request_util.request_infor(url)


        """匹配结果"""
        Phone,Address,Gender,IP = spider_function.func(content)

        if Phone!=[] or Address!=[] or Gender!=[] or IP !=[]:
            """数据库操作"""
            DB_util.MongoDBAdd(Phone, Address, Gender, IP, conn, Email_Search)
            print "结果为：", Phone, Address, Gender, IP, "\n已存储到数据库中"
        else:
            print "无法查询到相关信息"
if __name__ == '__main__':
    main()