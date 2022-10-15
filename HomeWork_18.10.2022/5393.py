def checker(a):
    return a[3] ** 3 >= 2 * (a[1] * a[0] * a[2]) and a[0] > 10

file = open('9.txt')
maimSpisok = []
for i in file.readlines():
    spisok = [int(x) for x in i.split()]
    spisok.sort()
    if checker(spisok):
        maimSpisok.append(1)
print(len(maimSpisok))