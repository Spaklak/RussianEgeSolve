for a in range(1,1000):
    p = 1 
    for x in range(1,1000):
        b = (x % a == 0) <= ((x % a == 0) <= (x % 34 == 0) and (x % 51 == 0))
        p = p * b
    if p == 1:
        print(a)
        break