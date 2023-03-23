f = open('18.txt')
a = []
for i in f.readlines():
    i = list(map(int, i.split()))
    a.append(i)
mx = []
s = []
def f(stroka, stolb, count):
    global b
    if (stolb+1)<15 and a[stroka][stolb] < a[stroka][stolb+1]:
        b += f(stroka, stolb+1, count+a[stroka][stolb+1])
    if (stroka+1)<15 and a[stroka][stolb] < a[stroka+1][stolb]:
        b +=  f(stroka+1, stolb, count+a[stroka+1][stolb])
    if (stolb-1)>=0 and a[stroka][stolb] < a[stroka][stolb-1]:
        b += f(stroka, stolb-1, count+a[stroka][stolb-1])
    if (stroka-1)>=0 and a[stroka][stolb] < a[stroka-1][stolb]:
        b += f(stroka-1, stolb, count+a[stroka-1][stolb])
    s.append(count)
    return count
for i in range(0,15):
    for j in range(0,15):
        b = 0        
        f(i,j,a[i][j])
        mx.append(b)


print(max(s))