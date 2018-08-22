#coding:utf-8
from pymongo import MongoClient





def MongoDBConnect(DataBaseName,CollectionName,localhost,PortNumb):
    """数据库连接"""
    conn = MongoClient(localhost, PortNumb)
    Collection = conn[DataBaseName][CollectionName]
    return Collection


def MongoDBAdd(Name, Email, Address, Age, Phone, Ip,Collection):
    """增加一条数据"""
    i = MongoDBSort(Collection)
    for t_Name,t_Email,t_Address,t_Age,t_Phone,t_IP in zip(Name, Email, Address, Age, Phone, Ip):
        Collection.insert(
            {"_id": i, "Name": t_Name, "Email": t_Email, "Address": t_Address, "Age": t_Age,"Phone":t_Phone,"IP":t_IP})
        i = i + 1

def MongoDBSort(Collection):
    """选取数据库中id最大值"""
    i = Collection.find().sort("_id", -1).count()
    return i


def MongoDBfindifExists(Collection,Content,Type):
    """查询数据库中是否已有"""
    if Type == 'Email':
        for exist in Collection.find({'Email':{'$regex':Content,'$options':'i'}}):
            if exist != None:
                return exist
            else:
                return 0
    elif Type == 'Phone':
        for exist in Collection.find({'Phone':Content}):
            if exist != None:
                return exist
            else:
                return 0
    elif Type == 'IP':
        for exist in Collection.find({'IP':Content}):
            if exist != None:
                return exist
            else:
                return 0