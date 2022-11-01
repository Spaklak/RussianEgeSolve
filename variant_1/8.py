count = 0
for s in 'ABCDX':
    for s1 in 'ABCDX':
        for s2 in 'ABCDX':
            for s3 in 'ABCDX':
                i = s + s1 + s2 + s3
                if i.count('X') == 1:
                    count += 1
print(count)