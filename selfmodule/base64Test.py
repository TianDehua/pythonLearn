import base64

# 字节码在python中表示,前面要加b，例如 b'abcd'
enc1 = base64.b64encode(b'abcd')
print(type('abcd'))
print(type(b'abcd'))
print(enc1)

dec1 = base64.b64decode(b'YWJjZA==')
print(dec1)

# "url safe"的base64编码，把字符+和/分别变成-和_
enc2 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(enc2)
# 注意对比两者的不同
enc3 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(enc3)

dec = base64.urlsafe_b64decode('abcd--__')
print(dec) #返回 b'i\xb7\x1d\xfb\xef\xff'
# \xb7 是十六进制的表现形式，同0xb7