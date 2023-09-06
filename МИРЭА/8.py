count = 0
for a in range(-1000, 1000):
    p = True
    for x in range(1,1000):
        if p:
            for y in range(1,1000):
                p = ((x < 5) <= (x**2 < a)) and ((y**2 <= a) <= (y<=5))
                if p == False:
                    break
    if p:
        count += 1

print(count) # 19