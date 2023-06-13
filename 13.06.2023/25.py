import fnmatch

for i in range(0,10**9, 2023):
    if fnmatch.fnmatch(str(i), '20*23'):
        count = 0
        for x in str(i):
            count += int(x)
        
        if count < 20 and count % 7 == 0:
            print(i)

