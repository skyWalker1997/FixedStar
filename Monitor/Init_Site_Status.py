#coding:utf-8


from Util.OutputColor_Util import Logger
from Util import Site_Util

"""Edit your local path"""
JSON_PATH = "/Users/PINKFLOYD/Desktop/CodingStaff/PythonCoding/FixedStar_Json/Monitor/SiteInfo.json"

print Logger.WARNING + "*********************************************" + Logger.ENDC
print Logger.WARNING + "****This script is used in checking work ****" + Logger.ENDC
print Logger.WARNING+ "*********************************************" + Logger.ENDC
# 使用minidom解析器打开XML文档
readtemp = Site_Util.Read_Json(JSON_PATH)
Site_Util.initSiteStatus(readtemp,JSON_PATH)