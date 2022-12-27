data = open('27A.txt')
'''
100 10000
'''
spisok = [int(x) for x in data.read().split()]
spisokSum = []
for i in range(100):
    count = 0
    summ = 0
    for x in range(i, len(spisok)):
        if spisok[x] + summ <= 10000:
            count += 1
            summ += spisok[x]
        else:
            spisokSum.append(count)
            break

print(max(spisokSum))

data.close()

data = open('27B.txt')
'''
1200050 2000000
'''
spisok = [int(x) for x in data.read().split()]
spisokSum = []
for i in range(1200050):
    count = 0
    summ = 0
    for x in range(i, len(spisok)):
        if spisok[x] + summ <= 2000000:
            count += 1
            summ += spisok[x]
        else:
            spisokSum.append(count)
            break

print(max(spisokSum))

#работает только для файла A
