#!/usr/bin/python
# coding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom
import Site


from Util import XML_Util
from Util import Spider_Util
from Util.OutputColor_Util import Logger



"""Edit your local path"""
__XML__PATH__ = "./Site_Info.xml"

# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse(__XML__PATH__)
Data = DOMTree.documentElement
if Data.hasAttribute("data"):
    print Logger.HEADER + "*********************************************" + Logger.ENDC
    print Logger.HEADER + "***This is an application about monitoring***" + Logger.ENDC
    print Logger.HEADER + "***Threat Intelligence Source Site Status ***" + Logger.ENDC
    print Logger.HEADER + "*********************************************" + Logger.ENDC
    print Logger.LOGBLUE+ "\n\nRunning……\n\n" + Logger.ENDC
WebSites = Data.getElementsByTagName("Site")



if __name__ == '__main__':
    init_site = Site
    SiteStatusList = []
    for tempsite in WebSites:
        site = XML_Util.GetSite(tempsite, init_site)
        ConsultResult = Spider_Util.Consult(site)
        # print ConsultResult

        if str(ConsultResult).find(str(site.ExampleOutPut)) != -1:
            print Logger.OKGREEN + "Site: " + site.SiteName + " Available" + Logger.ENDC
            if cmp(str(site.SiteStatus).encode('utf-8'),"Unavailable")==0:
                #XML_Util.setWebStatus(tempsite,"Available")
                SiteStatusList.append({"Site":site.SiteName,"Status":"Available"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
        else:
            print Logger.FAIL + "Site: " + site.SiteName + " Unavailable" + Logger.ENDC
            if cmp(str(site.SiteStatus).encode('utf-8'),"Available")==0:
                #XML_Util.setWebStatus(tempsite,"Unaulable")
                SiteStatusList.append({"Site": site.SiteName, "Status": "Unavailable"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
        print Logger.BEGINC+Logger.PINK + "**************************" + Logger.ENDC
    XML_Util.setWebStatus(SiteStatusList,DOMTree,__XML__PATH__)
    XML_Util.setCheckDate(DOMTree,__XML__PATH__)