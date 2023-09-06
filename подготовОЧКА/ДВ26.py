#9999 978

data = open('26DV.txt')
data = [int(x) for x in data.read().split()]
data.sort()
data = data[::-1]
summa = 0
for i in range(978):
    summa += data[i]

print(summa, data[i])