#coding:utf-8

from Spiders.ThatsThem import all_function
from Spiders.ThatsThem.util import input_util, DB_util, Request_util

"""数据库信息"""
portnumb = 27017
hostname = "localhost"
DataBaseName = "Spider"
CollectionName = "ThatsThem"





def main():
    """"""

    """连接数据库"""
    conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)

    information_input = raw_input()
    """判断输入类型"""
    if(input_util.validateEmail(information_input)==1):
        print "输入为邮箱"
        output = DB_util.MongoDBfindifExists(conn, information_input, "Email")
        if output != None:
            print "Database:",output
        else:
            url = 'https://thatsthem.com/email/' + information_input
            message = Request_util.request_infor(url)
            Name, Email, Address, Age, Phone, Ip= all_function.func(message)
            print Name, Email, Address, Age, Phone, Ip
            DB_util.MongoDBAdd(Name, Email, Address, Age, Phone, Ip, conn)
    elif(input_util.validatePhone(information_input) == 1):
        print "输入为电话"
        output = DB_util.MongoDBfindifExists(conn, information_input, "Phone")
        if output != None:
            print "Database:", output
        else:
            url = 'https://thatsthem.com/phone/' + information_input
            message = Request_util.request_infor(url)
            Name, Email, Address, Age, Phone, Ip = all_function.func(message)
            print Name, Email, Address, Age, Phone, Ip
            DB_util.MongoDBAdd(Name, Email, Address, Age, Phone, Ip, conn)
    elif(input_util.validateIP(information_input)):
        print "输入为IP"
        output = DB_util.MongoDBfindifExists(conn, information_input, "IP")
        if output != None:
            print "Database:", output
        else:
            url = 'https://www.usphonebook.com/' + information_input+'/detailed'
            message = Request_util.request_infor(url)
            Name, Email, Address, Age, Phone, Ip = all_function.func(message)
            print Name, Email, Address, Age, Phone, Ip
            DB_util.MongoDBAdd(Name, Email, Address, Age, Phone, Ip, conn)
    else:
        print "数据输入有误"
if __name__ == '__main__':
    main()


