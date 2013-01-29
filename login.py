#!/usr/bin/env python
# coding:utf-8
import requests

r1 = requests.post('http://210.27.12.1:90/login.jsp')
jid = r1.cookies['JSESSIONID']

url = 'http://210.27.12.1:90/j_security_check' 
payload = 'j_username=1203121588&j_password=dc902014'
headers = {'Referer':'http://210.27.12.1:90/login.jsp;jsessionid='+jid,
			'Host':'210.27.12.1:90',
			'Origin': 'http://210.27.12.1:90',
			'Cookie': 'JSESSIONID='+jid
	}
r2 = requests.post(url,data = payload,headers=headers)


print r2.status_code
print r2.headers
print r2.text







# get cookie
#url = 'http://210.27.12.1:90/login.jsp'
#r = requests.post(url)
#cookie = r.cookies['JSESSIONID']

# login
#url = 'http://210.27.12.1:90/j_security_check'
#payload = {'j_username':'1203121588','j_password':'dc902014'}
#headers = {'JSESSIONID':cookie}
#r = requests.post(url,data=payload,headers=headers)

#print r.headers
#print r.text
