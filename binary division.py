def to2(x):
    b = []
    while x:
        b.append(x & 1)
        x >>= 1
    return b

def to10(b):
    r = 0
    for i in range(len(b)-1,-1,-1):
        r = (r + b[i]) << 1    
    return r >> 1

def bplus(b1,b2):
    l = len(b1)
    f = 0
    r = []
    for i in range(l):
        x = b1[i] + b2[i] + f
        f = x >> 1
        r.append(x & 1)
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

def bsub(b1,b2):
    r = bplus(b1,complement(b2))
    i = len(r)
    while not r[i - 1]:
        i -= 1
        if i == 0:
            return []
    return r [:i]

def notless(b1,b2):
    l1 = len(b1)
    l2 = len(b2)
    if l1 > l2:
        return 1
    if l1 < l2:
        return 0
    for i in range(l1 - 1,-1,-1):
        if b1[i] > b2[i]:
            return 1
        if b1[i] < b2[i]:
            return 0
    return 1

def bdiv(b11,b2):
    b1 = b11[:]
    l1 = len(b1)
    l2 = len(b2)
    r = [0 for i in range(l1)]
    while notless(b1,b2):
        b3 = b1[l1 - l2:l1] 
        if notless(b3,b2):
            r[l1 - l2] = 1
            b3.append(0)
            b4 = bsub(b3,b2 + [0])
            b1 = b1[:l1 - l2] + b4
            l1 = len(b1)
        else:
            r[l1 - l2 - 1] = 1
            b3.append(0)
            b3 = [b1[l1 - l2 -1]] + b3
            b4 = bsub(b3,b2 + [0,0])
            b1 = b1[:l1 - l2 - 1] + b4
            l1 = len(b1)
    #没去前导0
    return r,b1

x = int(input())
y = int(input())
r1,r2 = bdiv(to2(x),to2(y))
print("%d %d" % (to10(r1),to10(r2)))