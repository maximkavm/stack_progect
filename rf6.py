def rf(N):
    if N == 0:
        return '= 0'
    else:
        return rf(N-1)


print(rf(5))