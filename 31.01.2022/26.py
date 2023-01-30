data = open('26.txt')
#3900 4000
data = [int(x) for x in data.read().split()]
summa = 0
data.sort()
count = 0
for i in data:
    if i + summa <= 3900:
        count += 1
        summa += i
    else:
        break
print(count, data[-2] + data[-1])