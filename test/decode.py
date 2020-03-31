







# 通用解密方法
from hashids import Hashids
text='ra2JXPvnqEPWE9gm'
hash_ids = Hashids(salt='&-yx879yzi99tmum0s(e3+st85_+2g=u$e7cie2n$s_%@h@*k)9', min_length=16)
result = hash_ids.decode(text)

print(result)
print('---------------')








