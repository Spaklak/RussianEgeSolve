data = open('17.txt')
data = [int(x) for x in data.read().split()]
count = []
maxim = -100000
for i in data:
    if len(str(abs(i))) == 3:
        maxim = max(maxim, i)

for i in range(len(data)-1):
    if (len(str(abs(data[i]))) == 3 and len(str(abs(data[i+1]))) != 3) or (len(str(abs(data[i]))) != 3 and len(str(abs(data[i+1]))) == 3):
        if (data[i] + data[i+1]) <= maxim:
            count.append(data[i]+data[i+1])

print(len(count), max(count))
