data = open('18(1).txt')
a = []
for i in data.readlines():
    a.append([int(x) for x in i.split()])

t = open('18(2).txt')
check = []
for i in t.readlines():
    check.append([int(x) for x in i.split()])

s = []


def f(stroka, stolb, count):
    if  ((stolb+1) < 10) and a[stroka][stolb+1] in check:
        f(stroka,stolb+1, count + (a[stroka][stolb+1]))
    if ((stolb+1) < 10)  and a[stroka][stolb+1] not in check:
        f(stroka,stolb+1, count + (a[stroka][stolb+1]*2))
    if  ((stroka+1) < 10) and a[stroka+1][stolb] in check:
        f(stroka+1,stolb, count + (a[stroka+1][stolb]))
    if ((stroka+1) < 10) and a[stroka+1][stolb] not in check:
        f(stroka+1,stolb, count + (a[stroka+1][stolb]*2))
    
    if stroka == 9 and stolb == 9:
        s.append(count)


f(0,0,a[0][0])

print(min(s), max(s))