from functools import lru_cache # библиотека для ускорения рекурсии 
import sys
sys.getrecursionlimit(10000) 
'''
sys.getrecursionlimit(10000) позволяет увеличить глубину рекурсии
'''
@lru_cache(None) # статичный метод, который нужен для ускорения рекурсии
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n / 5 + 1)
    if n > 5 and n % 5 != 0:
        return n+f(n+6)

'''
Весь смысл задания - переписать условие. Если вы не можете переписать условие, то рекомендую прочитать это:
https://digitology.tech/docs/python_3/tutorial/index.html
'''

for i in range(1,1000): # специальное условие для задачи (используется только для задач Полякова)
    try:
        if f(i) > 1000:
            print(i)
            break
    except:
        pass
'''
Обычно в конце вам нужно будет узнать значение рекурсии. 
Допустим вам нужно узнать значение рекурсии для f(244). Тогда вы просто напишите:
print(f(244))
На этом ваша задача закончится
'''