
class Site():
    """
    Define Class Site
    """
    def __init__(self):
        self.SiteName = ""
        self.RequstType = ""
        self.GetInfoTpye = ""
        self.GetInfoEntry = ""
        self.SiteIllustrate = ""
        self.SiteUrl = ""
        self.Regex = ""
        self.ExampleInPutType = ""
        self.ExampleInPut = ""
        self.ExampleOutPut = ""
        self.TimeOut = ""
        self.SiteStatus = ""
        self.LastCheckDate = ""

    def PrintSiteInfo(self):
        """
        Print site information
        :return:None
        """
        print "****************"
        print self.SiteName
        print self.RequstType
        print self.GetInfoTpye
        print self.GetInfoEntry
        print self.SiteIllustrate
        print self.SiteUrl
        print self.Regex
        print self.ExampleInPutType
        print self.ExampleInPut
        print self.ExampleOutPut
        print self.TimeOut
        print self.SiteStatus
        print self.LastCheckDate


    def GetSiteStatus(self):
        return self.SiteStatus

    def GetSiteLastCheck(self):
        return self.LastCheckDate
