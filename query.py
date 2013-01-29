#!/usr/bin/env python
# coding:utf-8
import requests
import re

# http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20120514sn1585&degreecourseno=0821005

def getScore(url,stu,course):
	payload = {'studentid' : stu, 'degreecourseno' : course}

	r = requests.get(url, params = payload)

	start = r.text.find('<tbody>')
	end = r.text.find('</tbody>')
	tbody = r.text[start:end]

	val = []
	while '</td>' in tbody:
		end = tbody.find('</td>')
		start = tbody.rfind('>',0,end)
		val.append(tbody[start+1:end].strip())
		tbody = tbody[end+len('</td>'):]
	
	return val

if __name__ == '__main__':
	url = 'http://210.27.12.1:90/queryDegreeScoreAction.do'
	stu = 'xdleess20120514sn1585'
	course = '0321022'
	for s in getScore(url,stu,course):
		print s,

 
