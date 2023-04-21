print('p1,p2,p3,p4')
for p1 in range(2):
    for p2 in range(2):
        for p3 in range(2):
            for p4 in range(2):
                if ((p3 <= p1) <= (p4 or (not(p2)))) == 0:
                    print(p1,p2,p3,p4,sep='|')