data = open('24.txt')
glas = ['A', 'O']
sgl = ['B','C','D']
count = 0
a = []
spisok = data.read()
for i in range(len(spisok)):
    if i > 0:
        if spisok[i] in glas and spisok[i-1] in sgl:
            count += 1
        elif spisok[i] in sgl and spisok[i-1] in glas:
            pass
        else:
            a.append(count)
            count = 0
print(max(a))