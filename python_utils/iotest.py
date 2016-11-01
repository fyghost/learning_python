import json
d = dict(name='Bob', age=20, score=88)
l = ['abcd', 1, 2, 3] 
print(json.dumps(d))
dic = json.loads(json.dumps(d))
print(dic)
print(l) 