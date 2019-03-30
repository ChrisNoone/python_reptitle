# coding: utf-8

from urllib import request,parse
import json

base_url = 'https://fusion.spmobileapi.net/api/General/captcha'

req = request.Request(base_url, data={}, headers={})
rsp = request.urlopen(req)
json_data = rsp.read().decode('utf-8')
json_data = json.loads(json_data)
print(json_data['data'])
