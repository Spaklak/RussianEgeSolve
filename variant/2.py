print('a,b,c,d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (d and ((a or (not(c))) <= (a and b and (not(c))))) == 1:
                    print(a,b,c,d, sep='|')