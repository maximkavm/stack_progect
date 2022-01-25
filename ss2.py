def to_ss(N, p):
    S = 0
    D = 0
    if str(N).isnumeric():
        N = int(N)
        while N != 0:
            M = N % 10
            N = N // 10
            D = D + M * (p ** S)
            S += 1
    else:
        while len(N) != 0:
            M = N[-1:]
            N = N[:-1]
            if M == 'A':
                M = 10
            elif M == 'B':
                M = 11
            elif M == 'C':
                M = 12
            elif M == 'D':
                M = 13
            elif M == 'E':
                M = 14
            elif M == 'F':
                M = 15
            D = D + M * (p ** S)
            S += 1
        return D


# N = input()
# p, q = map(int, input().split())
S = 0
D = 0

print(to_ss(10101100, 10))
