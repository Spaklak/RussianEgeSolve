from functools import lru_cache

@lru_cache
def f(n,i):
    if n.count('CAC') < 3: # or n.count('CACAC') != 1
        try:
            return f(n + data[i],i+1)
        except:
            return len(n) if n.count('CAC') == 2 else  0
    else:
        return len(n)-1


data = open('24.txt')
data = data.read()
data = data.replace('B','C').replace('D','C').replace('F','C')
data = data.replace('E','A').replace('U','A')
a = []
for i in range(len(data)):
    a.append(f(data[i],i+1))

print(max(a))