#encoding:UTF-8
import urllib.request

url = "https://www.baidu.com"
data = urllib.request.urlopen(url).read()
d = data.decode('UTF-8')
print(d)