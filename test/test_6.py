import hashlib

f = open(r"D:\2.docx", 'rb')
data = f.read()
f.close()
print(data)
hash_sha1 = hashlib.sha1(data)
print(hash_sha1.hexdigest())