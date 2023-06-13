import sys

sys.setrecursionlimit(20000)


def f(n):
    if n > 3456: return n+1
    if n <= 3456 and n % 3 == 0:
        return f(n+1) + f(n+2)
    return f(n+n%3)+2

for i in range(1,20):
    f(i)

print(f(12)-f(17))