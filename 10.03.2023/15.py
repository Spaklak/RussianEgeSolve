potr = [2,4,6,8,10,12,14,16,18,20]
qotr = [5,10,15,20,25,30,35,40,45,50]
spisA = []
for a in range(2, 51):
    p = True
    spisA.append(a)
    for x in range(1,1000):
        p = ((x not in spisA) or (x in potr)) and ((x not in qotr) or (x not in spisA))
        if p == False:
            break
    if p:
        pass
    else:
        spisA.pop()

print(len(spisA), spisA)