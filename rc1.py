# Напишите рекурсивную процедуру, которая распечатывает в столбик числа от 1 до N.
def rf(n,m):
    print(n)
    if n < m:
        return rf(n + 1,m)
N = int(input())
rf(1,N)
