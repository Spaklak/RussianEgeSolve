file = open('9.txt')
maimSpisok = []
for i in file.readlines():
    spisok = [int(x) for x in i.split()]
    spisok.sort()
    if spisok[0] + spisok[3] == spisok[1] + spisok[2] and spisok[3] - spisok[0] < (spisok[1] + spisok[2]) - spisok[3]:
        maimSpisok.append(1)
print(len(maimSpisok))