import hashlib

#md5的使用
#MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib'.encode('utf-8'))
digest = md5.hexdigest()
print('md5 digest=', digest)

#sha1的使用
#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
#另外，还有sha256, sha512
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib'.encode('utf-8'))
digest = sha1.hexdigest()
print('sha1 digest=', digest)



