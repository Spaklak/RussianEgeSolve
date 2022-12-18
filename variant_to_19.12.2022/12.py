a = []
for i in range(251,1000):
    s = '5' * i
    while '55555' in s:
        s=s.replace('55555','88',1)
        s=s.replace('888','555',1)
    if s.count('5') == 1:
        print(i)
        break