#coding:utf-8
from Spiders.ThatsThem.util import DB_util

portnumb = 27017
hostname = "localhost"
DataBaseName = "Spider"
CollectionName = "ThatsThem"
conn = DB_util.MongoDBConnect(DataBaseName, CollectionName, hostname, portnumb)
DB_util.MongoDBAdd("1", "1", "1", "1", "1", "1", conn)