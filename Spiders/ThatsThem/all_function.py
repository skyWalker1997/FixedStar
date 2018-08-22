#coding:utf-8
import re

Name = []
Email = []
Address = []
Age = []
Phone = []
Ip = []


def func(content):
    pattern_email = re.compile(u'<span itemprop="email">(.*?)</span>', re.S)
    pattern_name = re.compile(u'<a href="/name/(.*?)">', re.S)
    pattern_address = re.compile(u'<a href="/address/(.*?)">', re.S)
    pattern_phone = re.compile(u'<span itemprop="telephone">(.*?)</span>', re.S)
    pattern_ip = re.compile(u'<a href="/ip/(.*?)">', re.S)
    pattern_age = re.compile(u'<span  class="active".*?>(.*?)</span>', re.S)

    result_email = re.findall(pattern_email, content)
    result_name = re.findall(pattern_name, content)
    result_address = re.findall(pattern_address, content)
    result_phone = re.findall(pattern_phone, content)
    result_ip = re.findall(pattern_ip, content)
    result_age = re.findall(pattern_age, content)

    for result in result_name:
        r_name = result
        Name.append(r_name.encode('utf-8'))
    # Count_Name = int(len(Name))
    # dict_info['Name'] = Name

    # print(Count)



    for result in result_address:
        r_address = result
        Address.append(r_address.encode('utf-8'))
    # Count_Address = int(len(Address))
    # dict_info['Address'] =  Address

    for result in result_age:
        r_age = result
        Age.append(r_age.encode('utf-8'))
    # Count_Age = int(len(Age))
    # dict_info['Age'] = Age




    for result in result_phone:
        r_phone = result
        Phone.append(r_phone.encode('utf-8'))
    # Count_phone = int(len(Phone))
    # dict_info['Phone'] = Phone


    for result in result_email:
        r_email = result
        Email.append(r_email.encode('utf-8'))
    # Count_Email = int(len(Email))
    # dict_info['Email_Format-Format'] =  Email

    for result in result_ip:
        r_ip = result
        Ip.append(r_ip.encode('utf-8'))
    # Count_Ip = int(len(Ip))
    # dict_info['IP'] = Ip


    # i = 0
    # print("分组打印")
    # for i in range(Count_Name):
    #    print("Name :",dict_info['Name'][i],"Address :",dict_info['Address'][i],"Name :",dict_info['Age'][i],"Name :",dict_info['Phone'][i]
    #          ,"Email_Format-Format :",dict_info['Email_Format-Format'][i],"IP :",dict_info['IP'][i])

    return Name, Email, Address, Age, Phone, Ip