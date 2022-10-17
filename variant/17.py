data = open('17.txt')
spisok = [int(x) for x in data.read().split()]
spisokEleven = []
countEleven = 0
spisokSeventyn = []
countSeventyn = 0
for i in spisok:
    if i % 11 == 0:
        countEleven += 1
        spisokEleven.append(i)
    if i % 17 == 0:
        countSeventyn += 1
        spisokSeventyn.append(i)

if countEleven > countSeventyn:
    print(countEleven, min(spisokEleven))
else:
    print(countSeventyn, min(spisokSeventyn))

data.close()