def checker(a):
    return a[0] ** 2 * 2 > a[1] * a[2] and a[1] != a[3] and a[2] != a[3] and len(a) != len(set(a))

file = open('9.txt')
maimSpisok = []
for i in file.readlines():
    spisok = [int(x) for x in i.split()]
    spisok.sort()
    if checker(spisok):
        maimSpisok.append(1)
print(len(maimSpisok))