data = open('24.txt').read()
count = 0
a = []
mainCount = 0
for i in range(len(data)):
    if data[i] == 'Z':
        if data[i+1] + data[i+2] == 'XY' or data[i+1] + data[i+2] == 'YX':
            mainCount += 1
            count = 0
    else:
        count += 1
    
    if count == 3:
        a.append(mainCount)
        count = 0
        mainCount = 0

print(max(a))