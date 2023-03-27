count = 0
for a in range(1,1000):
    p = True
    for x in range(1,1000):
        if p == False:
            break
        for y in range(1,1000):
            p = ((x < a) <= (x * x <= 169)) and ((y * y < 16) <= (y <= a))
            if p == False:
                break
    if p:
        count += 1
        print(a)

print(count)