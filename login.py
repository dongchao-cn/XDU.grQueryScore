#!/usr/bin/env python
# coding:utf-8
import requests
from query import getAllScore

def getStuid(body):
    pos = body.find('queryDegreeScoreAction.do')
    start = body.find("studentid=",pos) + len('studentid=')
    end = body.find("&",pos)
    return body[start:end]

def getCourses(body):
    course = []
    ele = body.split()
    for item in ele:
        if len(item) == 7 and item.isdigit():
            course.append(item)
    return course

if __name__ == '__main__':
    stuno = raw_input(u'please input id:')
    stupw = raw_input(u'please input password:')

    print u'qerying，please wait...'
    s = requests.Session()

    s.get('http://210.27.12.1:90/student/index.jsp')

    payload = 'j_username=' + stuno + '&j_password=' + stupw
    h2 = {
        'Content-Type': 'application/x-www-form-urlencoded',    # header里面必须要加这个参数，貌似那边服务器有验证
    }

    s.post('http://210.27.12.1:90/j_security_check',data = payload,headers=h2)

    r = s.get('http://210.27.12.1:90/student/main.jsp')
    stuid = getStuid(r.text)
    #print stuid
    
    r = s.get('http://210.27.12.1:90//viewStudyPlanAction.do')
    courses = getCourses(r.text)
    #print courses

    scores = getAllScore('http://210.27.12.1:90/queryDegreeScoreAction.do',stuid,courses)
    print u'课程名称,学分,成绩'
    for each in scores:
        print "%s,%s,%s" % (each[1], each[2], each[4])
    raw_input(u'press anykey to exit!')
