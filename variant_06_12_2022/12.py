count = 10000000000000000000000000
a = 0
for i in range(251,1000):
    s = '5' * i
    while '55555' in s:
        s = s.replace('55555','88',1)
        s = s.replace('888','555',1)
    if s.count('5') < count:
        count = s.count('5')
        a = i
print(a)