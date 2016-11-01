import urllib2
import urllib
import cookielib

# cookie = cookielib.CookieJar()
fileName = 'e:\\python\\cookie.txt'
cookie = cookielib.MozillaCookieJar(fileName)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
postdata = urllib.urlencode({
    'id': 'fyghost',
    'passwd': 'fy19920609'
})
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
headers = {
    'User-Agent': user_agent, 
    'accept': 'application/json', 
    'x-requested-with': 'XMLHttpRequest'
}
opener.addheaders = [('User-Agent', user_agent), ('accept', 'application/json'), ('x-requested-with', 'XMLHttpRequest')]
result = opener.open('https://bbs.byr.cn/user/ajax_login.json', postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
targetUrl = 'https://bbs.byr.cn/board/ParttimeJob'
result = opener.open(targetUrl)
page = result.read()
data = unicode(page, 'gbk').encode('utf-8')
print data
