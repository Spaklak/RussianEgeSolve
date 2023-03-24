data = open('18.txt')
a = []
for i in data.readlines():
    a.append([int(x) for x in i.split()])

s = []
def f(stroka, stolb, count):
    if (stolb+1) < 15 and a[stroka][stolb+1] != 0:
        f(stroka,stolb+1, count + a[stroka][stolb+1])
    if (stroka + 1) < 15 and a[stroka+1][stolb] != 0:
        f(stroka+1,stolb, count + a[stroka+1][stolb])
    
    if stroka == 14 and stolb == 14:
        s.append(count)


f(0,0,a[0][0])

print(min(s), max(s))