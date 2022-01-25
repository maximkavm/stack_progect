# Тип Set
# 1) отсутсвует порядок
# 2) хранит тольько уникальные элементы
# 3) быстро может определять, есть ли элемент во множестве или  нет
# 4) добавление, удаление и обращение к элементу за время O(1)


firstSet = {1, 2, 3, 4}
secondSet = {4, 3, 2, 1}
secondSet.discard(1)
nums1 = set(range(100))
print(firstSet)
print(secondSet)
print(nums1)
print(type(nums1))
if 4 and 5 in firstSet:
    print('YES')
else:
    print('NO')

print('YES, include' if 2 and 3 in secondSet else 'NO')

lettersSet = set('Hello, world!')
lettersSet.add('1213')
print(*lettersSet)

lettersSet1 = {"Hello, world!"}
print(*lettersSet1)
# Операции над множествами
A = {1, 2, 3}
B = {3, 4, 5}
D = {10, 32}
# union объединение
print('union объединение')
C = A.union(B)
print(C)
print(C | D)

# intersection пересечение
print('intersection пересечение')
S = {10, 23}
K = D.intersection(S)
print(K)
print(A & B)

# difference разница
print('difference разница')
H = {1, 5, 62}
P = {1, 5, 61}
print(len(H))

print(H.difference(P))
print(P.difference(H))
print(H-P)
print(P-H)

print(H.symmetric_difference(P))
print(H^P)
