import json
from collections import OrderedDict

from Util.OutputColor_Util import Logger
from Util import Spider_Util
from Util import Site_Util
from Site import Site


__JSON_PATH__ = "/Users/PINKFLOYD/Desktop/CodingStaff/PythonCoding/FixedStar/Monitor/SiteInfo.json"

if __name__ == '__main__':
    print Logger.HEADER + "*********************************************" + Logger.ENDC
    print Logger.HEADER + "***This is an application about monitoring***" + Logger.ENDC
    print Logger.HEADER + "***Threat Intelligence Source Site Status ***" + Logger.ENDC
    print Logger.HEADER + "****************Version 0.0.2****************" + Logger.ENDC
    print Logger.HEADER + "*********************************************" + Logger.ENDC
    print Logger.LOGBLUE + "\n\n Running \n\n" + Logger.ENDC
    SiteStatusList = []

    readtemp = Site_Util.Read_Json(__JSON_PATH__)
    tempsite = Site.Site()
    for i in range(len(readtemp['site'])):
        site = Site_Util.Get_Site_Info(tempsite,readtemp,i)
        ConsultResult = Spider_Util.Consult(site)
        if str(ConsultResult).find(str(site.ExampleOutPut)) != -1:
            print Logger.OKGREEN + "Site: " + site.SiteName + " Available" + Logger.ENDC
            if cmp(str(site.SiteStatus).encode('utf-8'), "Unavailable") == 0:
                # XML_Util.setWebStatus(tempsite,"Available")
                SiteStatusList.append({"Site": site.SiteName, "Status": "Available"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
        else:
            print Logger.FAIL + "Site: " + site.SiteName + " Unavailable" + Logger.ENDC
            if cmp(str(site.SiteStatus).encode('utf-8'), "Available") == 0:
                # XML_Util.setWebStatus(tempsite,"Unaulable")
                SiteStatusList.append({"Site": site.SiteName, "Status": "Unavailable"})
                print Logger.WARNING + "SiteStatus Changed!" + Logger.ENDC
        print Logger.BEGINC + Logger.PINK + "**************************" + Logger.ENDC
    Site_Util.Site_Config_Output(SiteStatusList,readtemp, __JSON_PATH__)
    # print SiteStatusList
    # for i in range(3):
    #     site = Get_Site_Info(readtemp, i)
    #     readtemp['site'][i]['sitestatus'] = "unavailable"
    #     Write_Site_Info(readtemp,JSON_PATH)