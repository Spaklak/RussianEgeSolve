s = '1' * 103

while '111' in s or '2222' in s:
    s = s.replace('111','22',1)
    s = s.replace('2222','1',1)

print(s)