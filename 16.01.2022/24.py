data = open('24.txt')
maxim = 0
d = data.read()
count = 1
for i in range(len(d)-1):
    if int(d[i]) < int(d[i+1]):
        count += 1
    else:
        maxim = max(maxim, count)
        count = 1

print(maxim)