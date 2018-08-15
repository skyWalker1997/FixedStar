#coding:utf-8

from Spiders.USPhoneBook import input_util, DB_util, Request_util, spider_function

"""数据库信息"""
portnumb = 27017
hostname = "localhost"
DataBaseName = "Spider"
CollectionName = "USPhoneBook"





def main():
    """"""

    """连接数据库"""
    conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)

    information_input = raw_input()
    """判断输入类型"""
    if(input_util.validatePhone(information_input)==1):
        print "输入为电话"
        output = DB_util.MongoDBfindifExists(conn, information_input, "Phone")
        if output != None:
            print "Database:", output
        else:
            url = 'https://www.usphonebook.com/' + information_input+'/detailed'
            message = Request_util.request_infor(url)
            Name, Address, Relatives, Associate = spider_function.func(message)
            print Name,Address,Relatives,Associate
            DB_util.MongoDBAdd(Name, Address, Relatives, Associate, information_input, conn)
    else:
        print "数据输入有误"
if __name__ == '__main__':
    main()


