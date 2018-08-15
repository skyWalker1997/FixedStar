#coding:utf-8
from pymongo import MongoClient
import spider_function




def MongoDBConnect(DataBaseName,CollectionName,localhost,PortNumb):
    """数据库连接"""
    conn = MongoClient(localhost, PortNumb)
    Collection = conn[DataBaseName][CollectionName]
    return Collection


def MongoDBAdd(Domain,Email,Collection):
    """增加一条数据"""
    i = MongoDBSort(Collection)
    Collection.insert(
        {"_id": i, "Domain": Domain, "Email": Email})
    i = i + 1


def MongoDBSort(Collection):
    """选取数据库中id最大值"""
    i = Collection.find().sort("_id", -1).count()
    return i


def MongoDBfindifExists(Collection,Domain):
    for exist in Collection.find({'Domain':Domain}):
        if len(exist)!= 0:
            return exist
        else:
            return 0