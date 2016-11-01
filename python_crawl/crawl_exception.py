import urllib2

url = 'https://bbs.byr.cn/section/ajax_list'
request = urllib2.Request(url)
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
    print e.msg