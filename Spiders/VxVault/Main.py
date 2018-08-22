#coding:utf-8

from Spiders.VxVault import input_util, Request_util, MD5_function, DB_util

"""数据库信息"""
portnumb = 27017
hostname = "localhost"
DataBaseName = "Spider"
CollectionName = "VXVualt"





def main():
    """"""

    """连接数据库"""
    conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)

    information_input = raw_input()
    """判断输入类型"""
    if(input_util.validateMD5(information_input)==1):
        print "输入为MD5"
        output = DB_util.MongoDBfindifExists(conn, information_input, "MD5")
        if output != None:
            print "Database:", output
        else:
            url = 'http://vxvault.net/ViriList.php'
            message = Request_util.request_infor(url, information_input)
            Date, URL, MD5, IP, Tools = MD5_function.MD5_func(message)
            print  Date, URL, MD5, IP, Tools
            DB_util.MongoDBAdd(Date, URL, MD5, IP, Tools, conn)
    else:
        print "数据输入有误"
if __name__ == '__main__':
    main()


