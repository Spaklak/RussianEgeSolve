data = open('24.txt')
data = data.read()
a = []
count = 0
for i in range(len(data)-2):
    if data[i] != data[i+1] and data[i+1] != data[i+2]:
        count += 1
    else:
        a.append(count)
        count = 0
print(max(a))