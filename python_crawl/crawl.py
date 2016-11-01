#encoding:UTF-8
import urllib2
import urllib

url = "https://bbs.byr.cn/user/ajax_login.json"
values = {'id': 'fyghost', 'passwd': 'fy19920609'}
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
headers = {'User-Agent': user_agent, 'accept': 'application/json', 'x-requested-with': 'XMLHttpRequest'}
# headers = {'User-Agent': user_agent, 'accept': 'application/json'}
data = urllib.urlencode(values)
getUrl = url + "?" + data
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
data = unicode(page, 'gbk').encode('utf-8')
print data