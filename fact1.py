# Напишите рекурсивную функцию, вычисляющую факториал числа.
def f1(n):
    if n == 1 return 1
    if n > 1:
        return f1(n - 1)


print(f1(11))
