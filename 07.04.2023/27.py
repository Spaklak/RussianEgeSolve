data = open('27-B.txt')
data = [int(x) for x in data.read().split()]
minim = []
for i in range(len(data)):
    for x in range(i+5, len(data)):
        minim.append(data[i] ** 2 + data[x] ** 2)

print(min(minim))