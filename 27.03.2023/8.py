simbol6 = []
simbol4 = []

for i in range(100000,1000000):
    n = [int(x) for x in str(i)]
    if len(set(n)) == len(n):
        if n[0] % 2 == 0 and n[1] % 2 != 0 and n[2] % 2 == 0 and n[3] % 2 != 0 and n[4] % 2 == 0 and n[5] % 2 != 0:
            simbol6.append(i)
        elif n[0] % 2 != 0 and n[1] % 2 == 0 and n[2] % 2 != 0 and n[3] % 2 == 0 and n[4] % 2 != 0 and n[5] % 2 == 0:
            simbol6.append(i)

for i in range(1000,10000):
    n = [int(x) for x in str(i)]
    if n[0] != n[1] and n[1] != n[2] and n[2] != n[3]:
        simbol4.append(i)

if len(simbol6) > len(simbol4):
    print(1, len(simbol6) - len(simbol4))
else:
    print(2, len(simbol4) - len(simbol6))