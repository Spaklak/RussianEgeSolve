data = open('24.txt')
count = 0
listcount = []
s = ''
for i in data.read():
    s += i
    if 'XZZY' in s:
        listcount.append(count)
        s = 'ZZY'
        count = 3
    else:
        count += 1
print(max(listcount))