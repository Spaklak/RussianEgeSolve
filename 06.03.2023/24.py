data = open('24.txt').read()
count = 0
listCount = []
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        count += 1
    else:
        listCount.append(count + 1)
        count = 0

print(max(listCount), listCount[-1])