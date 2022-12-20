for i in range(543210, 987655):
    dels = []
    maxim = 0
    minim = 100000000000000000000000000000000000000000000000
    for x in range(2,int(i**0.5)+1):
        if i % x == 0:
            maxim = max(maxim,abs(x - i // x))
            minim = min(minim,abs(x - i // x))
    if minim != 0 and minim != maxim and maxim != 0 and minim != 100000000000000000000000000000000000000000000000 and minim > 4444 and maxim % minim == 0:
        print(i, minim,sep='|')