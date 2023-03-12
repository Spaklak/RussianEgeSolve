data = open('24.txt').read()

mainCount = 0
count = 0

for i in data:
    count += 1
    if i == 'f':
        mainCount += 1
        if mainCount == 123:
            print(count)
            break