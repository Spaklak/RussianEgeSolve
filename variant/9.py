f = open('9.txt')
mainCount = 0
for s in f.readlines():
    d = [int(x) for x in s.split()]
    d.sort()
    if d[1] - d[0] == d[2] - d[1] and d[1] - d[0] != 0:
        mainCount += 1
print(mainCount)