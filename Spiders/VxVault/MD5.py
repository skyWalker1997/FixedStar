#coding:utf-8
import urllib
from urlparse import parse_qs
from wsgiref.simple_server import make_server

import requests

import MD5_function


def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    # 获取get中key为name的值
    MD5 = params.get('MD5', [''])[0]

    # 组成一个数组，数组中只有一个字典
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
    }

    test_data = {"MD5": MD5}
    test_data_urlencode = urllib.urlencode(test_data)

    url = "http://vxvault.net/ViriList.php"
    session = requests.session()
    requ = session.post(url, data=test_data_urlencode, headers=headers)
    result = MD5_function.MD5_func(requ.text)
    print result
    return str(result)



if __name__ == "__main__":
    port = 6088
    httpd = make_server("0.0.0.0", port, application)
    print "serving http on port {0}...".format(str(port))
    httpd.serve_forever()
