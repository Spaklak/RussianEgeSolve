data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
a=[]
for i in spisok:
    if i % 13 == 4 and i % 8 == 1:
        a.append(i)
print(max(a), sum(a))