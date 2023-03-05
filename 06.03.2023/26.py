# 10000

data = open('26.txt')

data = [int(x) for x in data.read().split()]
mainMass = 0
count = 0
for i in data:
    if 310 <= i <= 320:
        data.remove(i)
        count += 1
        mainMass += i
lastI = 0
data.sort()
for i in data:
    if mainMass + i <= 10000:
        mainMass += i
        count += 1
        lastI = i
    else:
        break
maxSum = 0
mainMass -= lastI
for i in data:
    if mainMass + i <= 10000:
        maxSum = max(maxSum,mainMass + i)

print(count, maxSum)