data = open('24DV.txt').read()
data = data.replace('B','A').replace('C','A')
listCount = []
count = 0
for i in range(len(data)):
    if data[i] == 'A':
        count = 1
        for x in range(i+1, len(data)):
            if data[x] == 'A':
                count += 1
            else:
                listCount.append(count)
                break

print(max(listCount))