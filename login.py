#!/usr/bin/env python
# coding:utf-8
import requests


header1 = {'Host':'gr.xidian.edu.cn',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'
    }


r1 = requests.get('http://gr.xidian.edu.cn',headers=header1)
print "111111111111111111111111111111111111"
print r1.status_code
print r1.headers
print r1.text
print r1.cookies

header2 = {
    'Host': '210.27.12.1:90',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Origin': 'http://gr.xidian.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    #'Cookie': 'JSESSIONID=' + jid,
}

r2 = requests.get('http://210.27.12.1:90/login.jsp',cookies=r1.cookies,headers=header2)
print "222222222222222222222222222222222222"
print r2.status_code
print r2.headers
print r2.text
print r2.cookies

payload = 'j_username=1203121588&j_password=dc902014'
header3 = {
    'Host': '210.27.12.1:90',
    'Connection': 'keep-alive',
    'Content-Length': str(len(payload)),
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Origin': 'http://210.27.12.1:90',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://210.27.12.1:90/login.jsp;jsessionid=' + r2.cookies['JSESSIONID'],
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    #'Cookie': 'JSESSIONID=' + jid,
}

r3 = requests.post('http://210.27.12.1:90/j_security_check',cookies=r2.cookies,data = payload,headers=header3)

print "333333333333333333333333333333333333"
print r3.status_code
print r3.headers
print r3.text
print r3.cookies
