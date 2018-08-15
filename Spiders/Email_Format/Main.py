#coding:utf-8

import DB_util
import Request_util
from Spiders.Email_Format import spider_function


def main():

    """数据库信息"""
    portnumb = 27017
    hostname = "localhost"
    DataBaseName  = "Spider"
    CollectionName = "Email_Format"


    """存储字段定义"""


    """报文构造"""
    print "请输入你想查询的邮箱域名"
    Email_Search = raw_input()

    """数据库连接"""
    conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)

    """搜索数据库中是否已有相关记录"""
    find = DB_util.MongoDBfindifExists(conn, Email_Search)
    if(find != None):
        print "Mongofind:"
    else:
        url = 'https://www.email-format.com/d/' + Email_Search
        content = Request_util.request_infor(url)


        """匹配结果"""
        Email = spider_function.func(content)

        if Email!=[]:
            """数据库操作"""
            DB_util.MongoDBAdd(Email_Search, Email, conn)
            print "结果为：", Email, "\n已存储到数据库中"
        else:
            print "无法查询到相关信息"
if __name__ == '__main__':
    main()