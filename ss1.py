N = int(input())
S = 0
D = 0
while N != 0:
    M = N % 10
    N = N // 10
    D = D + M*(2 ** S)
    S += 1

print(D)
