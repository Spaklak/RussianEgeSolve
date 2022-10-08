data = open('24.txt')
spisok = data.read()
s = ''
counter = 0
spisokCouner = []
count = 0
for i in spisok:
    s += i
    if count % 2 != 0:
        if (s[count-1] == 'B' or s[count-1] == 'C' or s[count-1] == 'D') and (s[count] == 'A' or s[count] == 'O'):
            counter += 1
        else:
            s = i
            count = 0
            spisokCouner.append(counter)
            counter = 0
    count += 1

print(max(spisokCouner))