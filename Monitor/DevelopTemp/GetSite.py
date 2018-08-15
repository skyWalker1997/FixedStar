from Monitor import Site

def GetSite(Infomation,site):

    for info in Infomation:

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
        site.ExampleInPut = ExampleInPut.childNodes[0].data

        ExampleOutPut = info.getElementsByTagName('ExampleOutput')[0]
        site.ExampleOutPut = ExampleOutPut.childNodes[0].data

        SiteStatue = info.getElementsByTagName('SiteStatue')[0]
        site.SiteStatus = SiteStatue.childNodes[0].data

        LastCheckDate = info.getElementsByTagName('LastCheckDate')[0]
        site.LastCheckDate = LastCheckDate.childNodes[0].data
        return site