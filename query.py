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

def getAllScore(url,stu,courses):
	scores = []
	for course in courses:
		scores.append(getScore(url,stu,course))
	return scores


if __name__ == '__main__':
	url = 'http://210.27.12.1:90/queryDegreeScoreAction.do'
	stu = 'xdleess20120514sn1585'
	courses = [
		'0022001',
		'0321003',
		'0321007',
		'0321011',
		'0321020',
		'0321022',
		'0322102',
		'0821001',
		'0821100',
		'0821101',
		'0022002',
		'0022004',
		'0321006',
		'0322208',
		'0821001',
		'0821005',
		'0821102',
		'0821004',
		]
	scores = getAllScore(url,stu,courses)
	print '课程名称,学分,成绩'
	for each in scores:
		print "%s,%s,%s" % (each[1], each[2], each[4])
