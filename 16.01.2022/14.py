s = 3 * 15**1140 + 2 *15 **1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
maxim = 0
mainCount = 0
a = []
count = 1 
while s: #123
    mainCount += 1
    a.append(s % 15)
    if a[mainCount-2] == a[mainCount-1]:
        count +=1
        s//=15
    else:
        maxim = max(maxim, count)
        count = 1
        s//=15
print(maxim)