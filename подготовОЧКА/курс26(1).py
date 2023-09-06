# 1000000 - free space
# 10000 - N
data = open('26_225.txt').read()
data = [int(x) for x in data.split()]
data.sort()
freeSpace = 0
small = 0
data = data[::-1]
count = 0
for i in data:
    if freeSpace + i <= 1000000:
        freeSpace += i
        small = i
        count += 1

print(count, small)