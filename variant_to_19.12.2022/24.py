data = open('24.txt')
s = ''
count = 0
a = []
for i in data.read():
    s += i
    if i == 'A':
        count += 1
    if count == 2:
        count = 0
        a.append(len(s))
        s = ''
print(max(a))