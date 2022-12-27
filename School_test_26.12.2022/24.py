data = open('24.txt')
s = ''
spisokcount = []
count = 0
for i in data.read():
    s += i
    if len(s) == 3:
        if 'ABC' in s or 'BAC' in s or 'CAB' in s or 'CBA' in s:
            count += 1
            s = i
        else:
            spisokcount.append(count)
            count = 0
            s = i
print(max(spisokcount))

# пока что не работает