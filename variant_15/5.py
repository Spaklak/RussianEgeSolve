count = 0
for i in range(300,401):
    n = sorted(str(i))
    minim = n[0] + n[1]
    maxim = n[2] + n[1]
    if int(maxim) - int(minim) == 20:
        count += 1
print(count)
