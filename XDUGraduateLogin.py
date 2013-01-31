import sys
import re
import urllib2
import urllib
import cookielib
def autoLogin(url, username, pwd):
	cookie=cookielib.CookieJar()
	cj=urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(cj)
	postdata = {'j_username':'1203121522',
				'j_password':'1203121522',
				}
	req = urllib2.Request('http://210.27.12.1:90/student/index.jsp')
	operate = opener.open(req)
	req = urllib2.Request(url, urllib.urlencode(postdata))
	operate = opener.open(req)
	return  operate.read();
content = autoLogin('http://210.27.12.1:90/j_security_check','1203121522','1203121522')
print content