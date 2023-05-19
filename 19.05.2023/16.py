import sys
sys.setrecursionlimit(2000)

def f(n):
    if n < 2: return 7
    if n > 1: return 7 * f(n-2)

print(f(20), 7 ** 11)
'''
берем в f целую часть от деления на 2 + 1
20 // 2 + 1 == 11
12950 // 2 + 1 = 6476
7**6476/7**6473 == 7 ** 3 = 343
'''