import re


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
        else:
            return 0
def validatePhone(phone):
    if len(phone) == 12:
        if re.match("(^\d\d\d)(-)(\d\d\d)(-)(\d\d\d\d)", phone) != None:
            return 1
        else:
            return 0
def validateIP(IP):
    if len(IP) > 7:
        if re.match("(\d{1,3})(.)(\d{1,3})(.)(\d{1,3})(.)(\d{1,3})",IP) != None:
            return 1
        else:
            return 0



"""def validateName(Name):
"""