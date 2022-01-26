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

print(H.difference(P))
# print(P.difference(H))
# print(H-P)
# print(P-H)
# print(H.symmetric_difference(P))
print(H^P)