def fto2(s):
    p = s.split(".")
    r = [[],[]]
    p1 = int(p[0])
    p2 = float("0." + p[1])
    while p1:
        r[0].append(p1 & 1)
        p1 >>= 1
    r[0].reverse()
    if r[0] == []:
        r[0].append(0)
    s = 0.0
    for i in range(1,26):
        power = 2 ** (-i)
        if s + power <= p2:
            r[1].append(1)
            s += power
        else:
            r[1].append(0)
    return r

def exp(x,num):
    x += 2 ** (num - 1) - 1
    r = []
    s = 0
    for i in range(num):
        power = 2 ** (num - i - 1)
        if s + power <= x:
            r.append("1")
            s += power
        else:
            r.append("0")
    return "".join(r)

def dec2float(x):
    sign = '0'
    if x[0] == '-':
        sign = '1'
        x = x[1:]
    if x.find(".") == -1:
        x += ".0"
    r = fto2(x)
    if len(r[0]) - 1 > 127:
        return "Overflow"
    i = 0
    while i < len(r[1]):
        if r[1][i] == 1:
            break
        i += 1
    if i + 1 > 126 or (i == len(r[1]) and r[0] == [0]):
        return "".join(["0" for i in range(32)])
    if r[0] != [0]:
        e = len(r[0]) - 1
    else:
        e = -i - 1
    r = r[0] + r[1]
    if r[24] == 1 and r[23] == 0:
        r[23] = 1
    return sign + exp(e,8) + "".join([chr(d + ord('0')) for d in r[1:24]])

num = lambda x:ord(x) - ord('0')

def to10(s):
    r = 0
    l = len(s)
    for i in range(l):
        r += 2 ** i * num(s[l-i-1])
    return r

def float2dec(x):
    if x[0] == 'O':
        return x
    for c in x:
        if c != '0':
            e = to10(x[1:9]) - 127
            r = 2 ** e
            for i in range(23):    
                r += 2 ** (e-i-1) * num(x[9 + i])
            if x[0] == '1':
                return -r
            return r
    return 0.0

r = dec2float(input())
print(r,float2dec(r))