b = []
for x in range(70,81):
    b.append(x)
count = 0
for a in range(1,10000):
    p = True
    for x in range(1,10000):
        p = (x % a == 0) or ((x in b) <= (not(x % 18 == 0)))
        if p == False:
            break
    if p:
        count += 1
print(count)