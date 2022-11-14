s = '1' + '0' * 105

while '10' in s:
    if '100' in s:
        s = s.replace('100', '1011',1)
    else:
        s=s.replace('10','11',1)

a = (hex(int(s,2))[2:])
count = 0
for i in a:
    if i == 'a':
        count += 10
    elif i == 'b':
        count += 11
    elif i == 'c':
        count += 12
    elif i == 'd':
        count += 13
    elif i == 'e':
        count += 14
    elif i == 'f':
        count += 15
    else:
        count += int(i)
print(count)