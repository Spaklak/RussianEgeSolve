a = [int(x) for x in range(150,251)]
count = 0
for i in range(2,1000000):
    n = bin(i)[2:]
    n += n[-2]
    n += n[1]
    if int(n,2) in a:
        count += 1
print(count)