import base64

str = b'binary\x00string'
print(base64.b64encode(str))