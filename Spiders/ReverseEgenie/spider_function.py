import re


def func(content):
    IP = []
    Address = []
    Gender = []
    Phone = []

    pattern_IP = re.compile(u'<th>Email-IP.*?<td>(.*?)</td>', re.S)
    pattern_State = re.compile(u'<th>State:.*?<td>(.*?)</td>', re.S)
    pattern_Address = re.compile(u'<th>Address.*?<td>(.*?)</td>', re.S)
    pattern_City = re.compile(u'<th>City:</th>.*?<td>(.*?)</td>', re.S)
    pattern_Gender = re.compile(u'<th>Gender.*?<td>(.*?)</td>', re.S)
    pattern_Phone = re.compile(u'<th>Phone.*?<td>(.*?)</td>', re.S)
    pattern_Phone2 = re.compile(u'<a.*?>(.*?)</a>', re.S)
    pattern_IP2 = re.compile(u'<a.*?>(.*?)</a>', re.S)
    # u'<a href="http://www.reversegenie.com/reverse_phone/863-424-7777/">863-424-7777</a>'

    result_IP = re.findall(pattern_IP, content)
    result_State = re.findall(pattern_State, content)
    result_City = re.findall(pattern_City, content)
    result_Gender = re.findall(pattern_Gender, content)
    result_Phone = re.findall(pattern_Phone, content)
    result_Address = re.findall(pattern_Address, content)

    for r_Phone,r_IP,r_State,r_City,r_Gender,r_Address in zip(result_Phone,result_IP,result_State,result_City,result_Gender,result_Address):
        r_Phone = str(re.findall(pattern_Phone2, r_Phone.encode('utf-8'))).replace('-', '').replace('\'', '')
        if (r_Phone == str('\-\\')):
            r_Phone = ''
        Phone.append(r_Phone)

        r_IP = str(re.findall(pattern_IP2, r_IP.encode('utf-8')))
        r_IP = r_IP.replace("[\'","").replace("\']","").replace("[]","")
        IP.append(r_IP)

        r_Gender = str(r_Gender).encode('utf-8')
        Gender.append(r_Gender)

        r_Address = str(r_State.encode('utf-8'))+'-'+str(r_City.encode('utf-8'))+'-'+str(r_Address.encode('utf-8'))
        Address.append(r_Address)
    return Phone,Address,Gender,IP