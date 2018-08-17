#coding:utf-8
import datetime

from OutputColor_Util import Logger


def GetSite(info,site):
    """
    Get infomation from xml
    :param info:
    :param site:
    :return site:
    """

    if info.hasAttribute("name"):
        print "Site: %s" % info.getAttribute("name")
        site.SiteName = info.getAttribute("name")
    # test = (Country.getElementsByTagName('rank')).length
    Request_Type = info.getElementsByTagName('Request_Type')[0]
    site.RequstType = Request_Type.childNodes[0].data

    GetInfoType = info.getElementsByTagName('GetInfoType')[0]
    site.GetInfoTpye = GetInfoType.childNodes[0].data

    SiteIllustrate = info.getElementsByTagName('SiteIllustrate')[0]
    site.SiteIllustrate = SiteIllustrate.childNodes[0].data

    SiteUrl = info.getElementsByTagName('SiteUrl')[0]
    site.SiteUrl = SiteUrl.childNodes[0].data

    Regex = info.getElementsByTagName('Regex')[0]
    site.Regex = Regex.childNodes[1].data

    ExampleInPut = info.getElementsByTagName('ExampleInput')[0]
    site.ExampleInPutType = ExampleInPut.getAttribute("type")
    site.ExampleInPut = ExampleInPut.childNodes[0].data

    ExampleOutPut = info.getElementsByTagName('ExampleOutput')[0]
    site.ExampleOutPut = ExampleOutPut.childNodes[0].data

    TimeOut = info.getElementsByTagName('TimeOut')[0]
    site.TimeOut = TimeOut.childNodes[0].data

    SiteStatus = info.getElementsByTagName('SiteStatus')[0]
    site.SiteStatus = SiteStatus.childNodes[0].data

    LastCheckDate = info.getElementsByTagName('LastCheckDate')[0]
    site.LastCheckDate = LastCheckDate.childNodes[0].data
    return site


def setWebStatus(SiteList,DOMTree,XMLPath):
    for site in SiteList:
        for j in range(0, DOMTree.childNodes[0].childNodes.length):
            if (cmp(str(DOMTree.childNodes[0].childNodes[j].nodeName), "Site") == 0):
                if (cmp(str(DOMTree.childNodes[0].childNodes[j].getAttribute("name")), site["Site"]) == 0):
                    for i in range(1, DOMTree.childNodes[0].childNodes[j].childNodes.length):
                        if (cmp(str(DOMTree.childNodes[0].childNodes[j].childNodes[i].nodeName).encode('utf-8'),
                                "SiteStatus") == 0):
                            # tag = DOMTree.childNodes[0].childNodes[j].childNodes[i].childNodes[0].nodeValue
                            DOMTree.childNodes[0].childNodes[j].childNodes[i].childNodes[0].nodeValue = site["Status"]

                            # print DOMTree.childNodes[0].childNodes[j].childNodes[i].childNodes[0].nodeValue

    with open(XMLPath, 'w') as fh:
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        #  第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        DOMTree.writexml(fh, indent='', addindent='', newl='', encoding='utf-8')
        #print Logger.OKGREEN+ '站点配置表更新!' + Logger.ENDC

def setCheckDate(DOMTree,XMLPath):
    for j in range(0, DOMTree.childNodes[0].childNodes.length):
        if (cmp(str(DOMTree.childNodes[0].childNodes[j].nodeName), "Site") == 0):
                for i in range(1, DOMTree.childNodes[0].childNodes[j].childNodes.length):
                    if (cmp(str(DOMTree.childNodes[0].childNodes[j].childNodes[i].nodeName).encode('utf-8'),
                            "LastCheckDate") == 0):
                        DOMTree.childNodes[0].childNodes[j].childNodes[i].childNodes[0].nodeValue = datetime.datetime.now().strftime('%Y-%m-%d')

                        # print DOMTree.childNodes[0].childNodes[j].childNodes[i]
    with open(XMLPath, 'w') as fh:
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        #  第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        DOMTree.writexml(fh, indent='', addindent='', newl='', encoding='utf-8')
        print Logger.OKGREEN + '站点配置表更新!' + Logger.ENDC
        print Logger.OKGREEN + 'Site_Info.xml Update!' + Logger.ENDC


def initSiteStatus(DOMTree,XMLPath):
    """To init the site status"""
    for j in range(0, DOMTree.childNodes[0].childNodes.length):
        if (cmp(str(DOMTree.childNodes[0].childNodes[j].nodeName), "Site") == 0):
                for i in range(1, DOMTree.childNodes[0].childNodes[j].childNodes.length):
                    if (cmp(str(DOMTree.childNodes[0].childNodes[j].childNodes[i].nodeName).encode('utf-8'),
                            "SiteStatus") == 0):
                        DOMTree.childNodes[0].childNodes[j].childNodes[i].childNodes[0].nodeValue = "Unavailable"
                        DOMTree.childNodes[0].childNodes[j].childNodes[i + 2].childNodes[0].nodeValue = "2018-8-14"
                        # print DOMTree.childNodes[0].childNodes[j].childNodes[i]
    with open(XMLPath, 'w') as fh:
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        #  第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        DOMTree.writexml(fh, indent='', addindent='', newl='', encoding='utf-8')
        print Logger.WARNING + '站点状态均已设为不可用!日期设置为2018-8-14！' + Logger.ENDC
        print Logger.WARNING + 'All site`s status are set to unavailable,lastcheckdate are set to 2018-8-14 ' + Logger.ENDC