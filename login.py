#!/usr/bin/env python
# coding:utf-8
import requests

s = requests.Session()

r1 = s.get('http://210.27.12.1:90/student/index.jsp')

payload = 'j_username=1203121588&j_password=dc902014'
h2 = {
    'Content-Type': 'application/x-www-form-urlencoded',    # header里面必须要加这个参数，貌似那边服务器有验证
}

r2 = s.post('http://210.27.12.1:90/j_security_check',data = payload,headers=h2)

r3 = s.get('http://210.27.12.1:90/student/main.jsp')
print r3.text
