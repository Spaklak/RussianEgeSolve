f = open('17.txt')
spisok = [int(x) for x in f.read().split()]
a = []
for i in spisok:
    if (i % 10 == 2 or i % 10 == 7) and i % 3 == 0 and i % 11 == 0:
        a.append(i)
print(len(a), min(a))