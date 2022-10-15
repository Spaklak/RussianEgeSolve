def checker(a):
    return a[0] * a[3] == a[1] * a[2] and a[2] ** 2 > a[0] * a[3]

file = open('9.txt')
maimSpisok = []
for i in file.readlines():
    spisok = [int(x) for x in i.split()]
    spisok.sort()
    if checker(spisok):
        maimSpisok.append(1)
print(len(maimSpisok))