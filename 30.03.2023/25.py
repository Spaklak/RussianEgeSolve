import fnmatch
count = 0
for i in range(0,10**7+1,159):
    if fnmatch.fnmatch(str(i), '2?1*67'):
        print(i, i // 159)

