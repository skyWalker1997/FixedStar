#coding:utf-8

"""Edit your local path"""
from xml.dom.minidom import parse
import xml.dom.minidom

from Util.OutputColor_Util import Logger
from Util import XML_Util

__XML__PATH__ = "./Site_Info.xml"
print Logger.WARNING + "*********************************************" + Logger.ENDC
print Logger.WARNING + "****This script is used in checking work ****" + Logger.ENDC
print Logger.WARNING+ "*********************************************" + Logger.ENDC
# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse(__XML__PATH__)
XML_Util.initSiteStatus(DOMTree,__XML__PATH__)