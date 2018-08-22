#coding:utf-8
import datetime
import json
from collections import OrderedDict

from OutputColor_Util import Logger


def Read_Json(JSON_PATH):
    with open(JSON_PATH, 'r') as f:
        readtemp = json.loads(f.read(), object_pairs_hook=OrderedDict)
        f.close()
        return readtemp


def Get_Site_Info(site,readtemp,i):
    site.SiteName = readtemp['site'][i]['sitename']
    site.RequstType = readtemp['site'][i]['requesttype']
    site.GetInfoTpye = readtemp['site'][i]['getinfotype']
    site.GetInfoEntry = readtemp['site'][i]['getinfoentry']
    site.SiteIllustrate = readtemp['site'][i]['siteillustrate']
    site.SiteUrl = readtemp['site'][i]['siteurl']
    site.Regex = readtemp['site'][i]['regex']
    site.ExampleInPutType = readtemp['site'][i]['exampleinputtype']
    site.ExampleInPut = readtemp['site'][i]['exampleinput']
    site.ExampleOutPut = readtemp['site'][i]['exampleoutput']
    site.TimeOut = readtemp['site'][i]['timeout']
    site.SiteStatus = readtemp['site'][i]['sitestatus']
    site.LastCheckDate = readtemp['site'][i]['lastcheckdate']
    return site


def Site_Config_Output(SiteList,readtemp,JSON_PATH):
    for i in range(len(readtemp['site'])):
        readtemp['site'][i]['lastcheckdate'] = datetime.datetime.now().strftime('%Y-%m-%d')
        for tempsite in SiteList:
            if (cmp(str(tempsite['Site']), str(readtemp['site'][i]['sitename'])) == 0):
                readtemp['site'][i]['sitestatus'] = tempsite['Status']
    Write_Site_Info(readtemp, JSON_PATH)

def initSiteStatus(readtemp,JSONPATH):
    for i in range(len(readtemp['site'])):
        readtemp['site'][i]['lastcheckdate'] = "2018-8-15"
        readtemp['site'][i]['sitestatus'] = "Unavailable"
    Write_Site_Info(readtemp,JSONPATH)

# def Change_Site_LastCheckDate(readtemp):
#     for i in range(len(readtemp['site'])):
#         readtemp['site'][i]['lastcheckdate'] = datetime.datetime.now().strftime('%Y-%m-%d')
#
#
# def Change_Site_Status(SiteList,readtemp,JSON_PATH):
#     for tempsite in SiteList:
#         for i in range(len(readtemp['site'])):
#             if(cmp(str(tempsite['Site']),str(readtemp['site'][i]['sitename'])) == 0):
#                 readtemp['site'][i]['sitestatus'] = tempsite['Status']
#     Write_Site_Info(readtemp,JSON_PATH)





def Write_Site_Info(readtemp,JSON_PATH):
    jsObj = json.dumps(readtemp,indent=4)
    with open(JSON_PATH, 'w') as f:
        f.write(jsObj)
        f.close()
    print Logger.OKGREEN + '站点配置表更新!' + Logger.ENDC
    print Logger.OKGREEN + 'SiteInfo.json Updated!' + Logger.ENDC

# if __name__ == '__main__':
#     with open(JSON_PATH, 'r') as f:
#         readtemp = json.loads(f.read(),object_pairs_hook=OrderedDict)
#         f.close()
#     for i in range(2):
#         site = Get_Site_Info(readtemp,i)
#         readtemp['site'][i]['sitestatus'] = "unavailable"
#         Write_Site_Info(readtemp)