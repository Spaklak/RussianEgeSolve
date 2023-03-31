a = []
def f(n):
    a.append(n+1)
    if n > 1:
        a.append(n+5)
        f(n-1)
        f(n-2)

f(30)
print(sum(a))