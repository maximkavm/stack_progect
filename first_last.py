# Максимальный - вперед
# Требуется поменять местами первый элемент массива с максимальным.
# Входные данные
# В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива. Во второй строке задаются N чисел
# – элементы массива (целые числа, не превосходящие по модулю 1000).
# Выходные данные
# Вывести получившийся массив. Если максимальных элементов несколько, требуется поменять
# первый из них.
# Sample Input:
# 5
# 1 2 3 4 5
# Sample Output:
# 5 2 3 4 1

N = int(input())
m = [int(i) for i in input().split()]

maxelm = m[0]
indmaxelm = 0
for i in range(0, N):
    if m[i] > maxelm:
        maxelm = m[i]
        indmaxelm = i

m[0], m[indmaxelm] = m[indmaxelm], m[0]
print(*m)
