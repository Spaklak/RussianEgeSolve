data = open('27ADV.txt')
data = [int(x) for x in data.read().split()]
count = 0
for i in range(len(data)):
    for x in range(i+1,len(data)):
        if ((data[i] + data[x]) > 50) and (data[x] > data[i]):
            count += 1

print(count)