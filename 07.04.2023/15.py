for a in range(1,1000):
    p = True
    for x in range(1,1000):
        p = (x % a == 0) or ((x % 23 == 0) <= (not(50 <= x <= 70)))
        if p == False:
            break
    if p:
        print(a)