count = 0
for x in range(0,120):
    for y in range(0,20):
            if y < 3*x and 0 < y < 15 and y > x/14:
                count += 1
print(count)