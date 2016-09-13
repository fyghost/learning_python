import hashlib

abstract = hashlib.md5()
abstract.update('what the fuck'.encode('utf-8'))
abstract.update('is that'.encode('utf-8'))
print(abstract.hexdigest())