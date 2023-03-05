data = open('17.txt')
data = [int(x) for x in data.read().split()]
a = []
minim8 = 100000000
minimSum = 10000000
for i in data:
    if i % 8 == 0 and i != 8:
        minim8 = min(i, minim8)

for i in range(len(data)-1):
    if data[i] % minim8 == 0 and data[i+1] % minim8 == 0:
        a.append([data[i] + data[i+1], max(data[i], data[i+1])])
        minimSum = min(minimSum,data[i] + data[i+1])
print(len(a))
for i in a:
    if i[0] == minimSum:
        print(i[1])
        break