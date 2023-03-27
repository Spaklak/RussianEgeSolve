import sys
sys.setrecursionlimit(3000)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 4 == 0:
        return n / 4 + f(n / 4 + 2)
    if n < 10000 and n % 4 != 0:
        return 1 + f(n+2)


for i in range(1,100):
    f(i)
f(3)
