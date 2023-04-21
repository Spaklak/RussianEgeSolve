spisok = []
for q in range(30,50):
    for a in range(1,q):
        for b in range(1,q):
            for c in range(1,q):
                for d in range(1,q):
                    if a < b < c < d:
                        x = (a * q ** 3) * (b * q ** 2) * (c * q ** 1) * (d * q ** 0)
                        spisok.append(x)
print(min(spisok))