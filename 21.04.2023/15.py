a = 1000000000000
for p1 in range(1,1000):
    for p2 in range(1,1000):
        p = True
        count = 0
        for x in range(1,1000):
            p = (((x**2 + x - 20) >= 0) or (p1 <= x <= p2)) and (((x ** 2 - 3*x - 18) <= 0) or (p1 <= x <= p2))
            if p:
                count += 1
                if count == 10:
                    break
            if p == False:
                break
        if p:
            a = min(a, p2-p1)
print(a)