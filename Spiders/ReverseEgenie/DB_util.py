#coding:utf-8
from pymongo import MongoClient
import spider_function




def MongoDBConnect(DataBaseName,CollectionName,localhost,PortNumb):
    """数据库连接"""
    conn = MongoClient(localhost, PortNumb)
    Collection = conn[DataBaseName][CollectionName]
    return Collection


def MongoDBAdd(Phone, Address, Gender, IP, Collection,Email_Search):
    """增加一条数据"""
    i = MongoDBSort(Collection)
    for t_Phone, t_Address, t_Gender, t_IP in zip(Phone, Address, Gender, IP):
        Collection.insert(
            {"_id": i, "Email": Email_Search, "IP": str(t_IP), "Gender": t_Gender, "Address": t_Address})
        i = i + 1

def MongoDBSort(Collection):
    """选取数据库中id最大值"""
    i = Collection.find().sort("_id", -1).count()
    return i


def MongoDBfindifExists(Collection,Email):
    for exist in Collection.find({'Email':Email}):
        if len(exist)!= 0:
            return exist
        else:
            return 0