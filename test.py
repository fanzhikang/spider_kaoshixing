# encoding: utf-8
__author__ = 'fanzhikang'
__date__ = '2018/10/18 23:13'

import requests
import json


login_data = {
    'userName': 'CECC511@cecctm.com',
    'userNameInput': 'CECC511',
    'newCompanyId': 5769,
    'password': '5c3a0d081b1bf8b462429e45f1c7d579',
    'remember': True
}
base_url = 'https://www.kaoshixing.com/account/login'
headers_base = {
        'Content-Type' : 'application/x-www-form-urlencoded',
    }
session = requests.session()
#登陆
content = session.post(base_url, headers = headers_base, data = login_data)
print(content.url)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = 'current=1&rowCount=10&searchPhrase=&status=&testType=&commitIds=&testDifficult=&testCreater=&testClassification=&testStartTime=&testEndTime=&fullText=&checkDup=0'
#请求列表
test_url = 'https://admin.kaoshixing.com/admin/showtestqm_grid/'
content = session.post('https://admin.kaoshixing.com/admin/showtestqm_grid/', headers=headers, data=data)
content = content.content.decode(encoding='utf-8')
content_dict = json.loads(content)
for li in content_dict['bizContent']['rows']:
    if li['type'] == '填空':
        classification = li['classification'].split('/')[-1]
        id = li['id']
        print('https://admin.kaoshixing.com/admin/load_data?&id=' + id)

    else:
        print('no')

data_url = "https://admin.kaoshixing.com/admin/load_data?&id=5b7a68c636098f6ee33300a0"
data_content = session.get(data_url)
data_content = data_content.content.decode(encoding='utf-8')


data_dict = json.loads(data_content)
if data_dict['bizContent'].get('key1', '') == '1':
    print("正确")

