def checker(a):
    return a[3] - a[0]  >= 50 and a[1] * a[2] <= 1000

file = open('9.txt')
maimSpisok = []
for i in file.readlines():
    spisok = [int(x) for x in i.split()]
    spisok.sort()
    if checker(spisok):
        maimSpisok.append(1)
print(len(maimSpisok))