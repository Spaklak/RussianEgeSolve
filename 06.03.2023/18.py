data = open('18.txt')
data = [float(x) for x in data.read().split()]
countList = []
count = []
for i in range(len(data)-1):
    if abs(data[i] - data[i+1]) >= 16:
        count.append(max(data[i], data[i] + data[i+1]))
    else:
        countList.append(sum(count))
        count = []

print(max(countList))