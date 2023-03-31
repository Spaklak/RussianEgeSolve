data = open('24.txt')
count = 0
for i in data.readlines():
    countB = i.count('B')
    countA = i.count('A')
    if ((countB - countA) / countA) * 100 > 5:
        count += 1
print(count)