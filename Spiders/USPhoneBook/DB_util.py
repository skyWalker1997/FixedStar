#coding:utf-8
from pymongo import MongoClient





def MongoDBConnect(DataBaseName,CollectionName,localhost,PortNumb):
    """数据库连接"""
    conn = MongoClient(localhost, PortNumb)
    Collection = conn[DataBaseName][CollectionName]
    return Collection


def MongoDBAdd(Name,Address,Relatives,Associate,Phone,Collection):
    """增加一条数据"""
    i = MongoDBSort(Collection)
    for t_Name,t_Address in zip(Name,Address):
        Collection.insert(
            {"_id": i, "Name": t_Name,"Phone":Phone,"Address": t_Address, "Relatives": Relatives, "Associate":Associate})
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