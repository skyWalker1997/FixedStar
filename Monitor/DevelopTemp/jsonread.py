# -*- coding:utf-8 -*-
import json
with open("DevelopTemp.json", 'r') as f:
  temp = json.loads(f.read())
  # print(temp['site'])
  for i in range(len(temp['site'])):
    print(temp['site'][i])




#
# d = dict(name = 'Bob',age = 20,score = 88)
# json.dump(d)
# print d