s = 0

def f(n):
    global s
    s += (n+1)
    if n > 1:
        s += (n+5)
        f(n-1)
        f(n-2)

f(30)
print(s)