f = open('24.txt')
f = f.read()
s = ''
spisok = [x for x in f]
count = 0
for i in spisok:
    s += i
    if i == 'B':
        if s[0] == 'A' and len(s) <= 15 and 'F' in s and s.count('A') == 1 and s.count('B') == 1:
            count += 1
            s = ''
        else:
            s = ''

print(count)
#неверно