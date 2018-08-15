#!/usr/bin/python
# coding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom
from Monitor.Site import Site
from Monitor.DevelopTemp import GetSite
from Monitor.Util import XML_Util, Spider_Util
from Monitor.Util.OutputColor_Util import Logger


# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse("test_data.xml")
Data = DOMTree.documentElement
if Data.hasAttribute("data"):
    print "*********************************************"
    print "***This is an application about monitoring***\n"\
          "***Threat Intelligence Source Site Status ***"
    print "*********************************************"
    print "\n\nRunning……\n\n"
WebSites = Data.getElementsByTagName("Site")



if __name__ == '__main__':
    site = Site.Site()
    SiteStatusList = []
    for tempsite in WebSites:
        site = XML_Util.GetSite(tempsite, site)
        ConsultResult = Spider_Util.Consult(site)
        # print ConsultResult
        if str(ConsultResult).find(str(site.ExampleOutPut)):
            print Logger.OKGREEN + "Site: " + site.SiteName + " available" + Logger.ENDC
            if cmp(str(site.SiteStatus),"Unavailable") == 0:
                #XML_Util.setWebStatus(tempsite,"Available")
                SiteStatusList.append({"site":site.SiteName,"status":"Available"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
        else:
            print Logger.FAIL + "Site" + site.SiteName + Logger.ENDC
            if cmp(str(site.SiteStatus),"Available"):
                #XML_Util.setWebStatus(tempsite,"Unaulable")
                SiteStatusList.append({"site": site.SiteName, "status": "Unavailable"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
    XML_Util.setWebStatus(SiteStatusList,DOMTree)