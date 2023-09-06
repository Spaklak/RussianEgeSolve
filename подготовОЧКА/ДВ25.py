import fnmatch
for i in range(0,10**8,2023):
    if fnmatch.fnmatch(str(i), '671??1*'):
        print(i,i//2023)