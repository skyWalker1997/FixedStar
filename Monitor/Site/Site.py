
class Site():
    """
    Define Class Site
    """
    def __init__(self):
        self.SiteName = ""
        self.RequstType = ""
        self.GetInfoTpye = ""
        self.SiteIllustrate = ""
        self.SiteUrl = ""
        self.ExampleInPut = ""
        self.ExampleOutPut = ""
        self.SiteStatus = ""
        self.LastCheckDate = ""

    def PrintSiteInfo(self):
        """
        Print site information
        :return:None
        """
        print self.SiteName
        print self.RequstType
        print self.GetInfoTpye
        print self.SiteIllustrate
        print self.SiteUrl
        print self.ExampleInPut
        print self.ExampleOutPut
        print self.SiteStatus
        print self.LastCheckDate

    def GetSiteStatus(self):
        return self.SiteStatus

    def GetSiteLastCheck(self):
        return self.LastCheckDate
