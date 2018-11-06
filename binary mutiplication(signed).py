#带符号的乘法 限制位数
def to2(x,num):
    if x < 0:
        return complement(to2(-x,num))
    r = []
    while x:
        r.append(x & 1)
        x >>= 1
    for i in range(num - len(r)):
        r.append(0)
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
    l1,l2 = len(b1),len(b2)
    l = max(len(b1),len(b2))+1
    r = []
    f = 0
    for i in range(l):
        x = f
        if i < l1:
            x += b1[i]
        if i < l2:
            x += b2[i]
        r.append(x & 1)
        f = x >> 1
    if r[l-1]:
        return r
    else:
        return r[:l-1]

def shl(b,d):
    r = b[:]
    while d:
        r = [0] + r
        d -= 1
    return r
def isZero(b,num):
    for i in range(num):
        if b[i]:
            return 0
    return 1

def mult(b1,b2,num):
    if isZero(b1,num) or isZero(b2,num):
        return [0 for i in range(num)]
    r = [0]
    for i in range(len(b2)):
        if b2[i]:
            r = plus(r,shl(b1,i))
    for i in range(num - len(r)):
        r.append(0)
    s1,s2,s3 = b1[num - 1],b2[num - 1],r[num - 1]
    if (s1 == s2 and not s3) or (s1 != s2 and s3):
        return r[:num]
    return [-1]

def to10(b,num):
    if b[num-1]:
        for i in range(num-1):
            if b[i]:
                return -to10(complement(b),num)
        return -2 ** (num-1)
    r = 0
    for i in range(num-1):
        r += 2 ** i * b[i]
    return r

a = int(input())
b = int(input())
if -2048 <= a <= 2047 and -2048 <= b <=2047:
    r = mult(to2(a,12),to2(b,12),12)
    if r[0] == -1:
        print("溢出错误")
    else:
        print(to10(r,12))
else:
    print("操作数超过范围")