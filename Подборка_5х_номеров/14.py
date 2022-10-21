count = 0
for i in range(1,1000000):
    s = 0
    if i % 3 == 0:
        s = i / 3
    else:
        s = i - 1
    if s % 5 == 0:
        s = s / 5
    else:
        s = s - 1
    if s % 11 == 0:
        s = s / 11
    else:
        s = s - 1
    if s == 8:
        count += 1
print(count)
# 4