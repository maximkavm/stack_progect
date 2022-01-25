def rf(N, S = 0):
    S += N % 10
    N = N // 10
    if N == 0:
        return S
    else:
        return rf(N, S)


print(rf(666))
