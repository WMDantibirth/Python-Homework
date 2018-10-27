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

def bmul(b1,b2):
    r = [0]
    for i in range(len(b2)):
        if b2[i]:
            r = bplus(r,shl(b1,i))
    return r

x = int(input())
y = int(input())
print(to10(bmul(to2(x),to2(y))))