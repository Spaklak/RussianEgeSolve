count = 0
for i in range(1,1000000):
    s = 0
    if i % 2 == 0:
        s = i / 2
    else:
        s = i - 1
    if s % 3 == 0:
        s = s / 3
    else:
        s = s - 1
    if s % 7 == 0:
        s = s / 7
    else:
        s = s - 1
    if s == 2:
        count += 1
print(count)
# 5