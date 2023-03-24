import fnmatch

for i in range(0,10**7+1,53):
    if fnmatch.fnmatch(str(i), '*2?2*'):
        if str(i) == str(i)[::-1]:
            dels = []
            for x in range(1,int(i**0.5)+1):
                if i % x == 0:
                    dels.append(x)
                    dels.append(i//x)
            if len(set(dels)) > 30:
                print(i, sum(dels))
