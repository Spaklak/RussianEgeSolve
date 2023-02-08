data = open('24.txt')
data = data.read()
data = data.replace('B','C').replace('D','C').replace('F','C')
data = data.replace('E','A').replace('U','A')
s = ''
mainly = 0
count = 0
mainCount = []
for i in range(len(data)):
    s = data[i]
    while s.count('CAC') < 3 or s.count('CACAC') != 1:
        try:
            i += 1
            s += data[i]
        except:
            break
    if len(s)-1 == 115:
        print(s)
    mainCount.append(len(s)-1)


print(max(mainCount))
