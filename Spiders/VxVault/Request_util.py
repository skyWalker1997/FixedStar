import urllib

import requests


def request_infor(url,MD5):
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
    }

    test_data = {"MD5": MD5}
    test_data_urlencode = urllib.urlencode(test_data)
    session = requests.session()
    requ = session.post(url, data=test_data_urlencode, headers=headers)
    return requ.text