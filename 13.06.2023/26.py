# 6200

data = open('26.txt').read()
data = [int(x) for x in data.split()]
countMax = []

data.sort()
for i in range(len(data)):
    ctrl = data[i]
    count = 1
    for x in range(i+1, len(data)):
        if data[x] - ctrl >= 8:
            count += 1
            ctrl = data[x]
    countMax.append(count)
    if count == 369:
        print(data[i])

print(max(countMax))
