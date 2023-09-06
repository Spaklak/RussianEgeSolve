def F(n):
    if n > 2:
        return F(n-1) + F(n-2)
    else:
        return 1

print(F(6)) # 8