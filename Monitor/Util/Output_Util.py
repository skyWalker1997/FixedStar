#coding:utf-8
import xml.dom.minidom


def PrintSiteInfo():
    """
    This function is to PRINT the information about
    Threat Intelligence Source Site
    :return:None
    """
    # 使用minidom解析器打开XML文档
    DOMTree = xml.dom.minidom.parse("../test_data.xml")
    Data = DOMTree.documentElement
    if Data.hasAttribute("data"):
        print "*********************************************"
        print "***Showing the SiteInfo***\n" \
              "***Threat Intelligence Source Site Status ***"
        print "*********************************************"
        print "\n\nRunning……\n\n"
    Countrys = Data.getElementsByTagName("Site")
    for Country in Countrys:
        print "*****Info*****"
        if Country.hasAttribute("name"):
            print "Site: %s" % Country.getAttribute("name")

        test = (Country.getElementsByTagName('rank')).length
        Request_Type = Country.getElementsByTagName('Request_Type')[0]
        print "Request_Type: %s" % Request_Type.childNodes[0].data
        GetInfoType = Country.getElementsByTagName('GetInfoType')[0]
        print "GetInfoType: %s" % GetInfoType.childNodes[0].data
        SiteIllustrate = Country.getElementsByTagName('SiteIllustrate')[0]
        print "SiteIllustrate: %s" % SiteIllustrate.childNodes[0].data
        SiteUrl = Country.getElementsByTagName('SiteUrl')[0]
        print "SiteUrl: %s" % SiteUrl.childNodes[0].data
        ExampleInput = Country.getElementsByTagName('ExampleInput')[0]
        print "ExampleInput: % s" % ExampleInput.childNodes[0].data
        ExampleOutput = Country.getElementsByTagName('ExampleOutput')[0]
        print "ExampleOutput: % s" % ExampleOutput.childNodes[0].data
        SiteStatue = Country.getElementsByTagName('SiteStatue')[0]
        print "SiteStatue: % s" % SiteStatue.childNodes[0].data
        LastCheckDate = Country.getElementsByTagName('LastCheckDate')[0]
        print "LastCheckDate: % s" % LastCheckDate.childNodes[0].data


if __name__ == '__main__':
    PrintSiteInfo()