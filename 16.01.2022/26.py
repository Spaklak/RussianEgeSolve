data = open('26.txt')
spisok =[]
mainCount = 0
for i in data.readlines():
    count = 0
    d = [int(x) for x in i.split()]
    for x in range(d[0],d[1]+1):
        if x in spisok:
            count += 1
        spisok.append(x)
    if count != 0:
        mainCount += 1

print(mainCount)