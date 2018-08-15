from pymongo import MongoClient

from Spiders.ReverseEgenie import DB_util

portnumb = 27017
hostname = "localhost"
DataBaseName  = "Spider"
CollectionName = "Reversegenie"
conn = MongoClient(hostname, portnumb)
Collection = conn[DataBaseName][CollectionName]
DB_util.MongoDBfindifExists(Collection, "Floridasun42@aol.com")
