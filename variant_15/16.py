from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - 2 * g(n-1)
@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + g(n-1) + n

a = g(36)
count = 0
for i in str(a):
    count += int(i)
print(count)