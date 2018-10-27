"""
类似习题 2.7，八位元CPU。
但是输入x, y 是介于-128 到127间的任意整数。
转为二进制后，做加法，如果有溢出，需要返回错误，否则返回十进制的结果。
此题的重点是负数补码，二进制加法，和判断溢出。
判断溢出必须用书上的方法，在二进制的结果上直接判断。
请同学试验各种情况，例如，64+65, 100+10, 100+(-128)，10+（-100）， （-30）+（-100）， （-127）+127
"""

def convert(x,d):
    r = [0 for i in range(d)]
    i = 0
    while x:
        r[i] = x & 1
        x >>= 1
        i += 1
    return r

def complement(b):
    r = [i ^ 1 for i in b]
    r[0] ^= 1
    if r[0]:
        return r
    else:
        for i in range(1,len(r)):
            r[i] ^= 1
            if r[i]:
                break
        return r

def plus(b1,b2):
    l = len(b1)
    f = 0
    r = []
    for i in range(l):
        x = b1[i] + b2[i] + f
        f = x >> 1
        r.append(x & 1)
    if not b1[l-1] ^ b2[l-1] and b2[l-1] ^ r[l-1]:
        raise OverflowError()
    else:
        return r
    
def convert2(b):
    l = len(b)
    if b[l-1]:
        return -convert2(complement(b))
    r = 0
    for i in range(l):
        r += 2 ** i * b[i]
    return r

x = int(input())
y = int(input())
if x < 0:
    b1 = complement(convert(abs(x),8))
else:
    b1 = convert(x,8)
if y < 0:
    b2 = complement(convert(abs(y),8))
else:
    b2 = convert(y,8)
try:
    print(convert2(plus(b1,b2)))
except OverflowError:
print("Overflow")