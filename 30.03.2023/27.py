data = open('27A.txt')

data = [int(x) for x in data.read().split()]
k = 0
for i in range(len(data)):
    chetnost = data[i] % 2
    for x in range(i+1, len(data)):
        if data[x] % 2 == chetnost:
            print(data[i], data[x])
            k += 1
print(k)
#2459