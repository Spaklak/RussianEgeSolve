s = 48835
count = 0
while s:
    if s % 2 == 1:
        count += 1
    s//=2
print(count) # 10