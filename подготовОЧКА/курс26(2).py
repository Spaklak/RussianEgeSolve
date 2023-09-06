# 5000 - D
# 1500 - E
# 20
data = open('26_788.txt').read()
data = [int(x) for x in data.split()]
data.sort()
data = data[::-1] # для второго ответа, в первом не юзать
sizeD = 0
sizeE = 0
listD = []
listE = []
count = 0
for i in data:
    if i > 500:
        if sizeD + i <= 5000:
            sizeD += i
            count += 1
            listD.append(i)
    if i <= 500:
        if sizeE + i <= 1500:
            sizeE += i
            count += 1
            listE.append(i)

print(count, max(listD) + max(listE))