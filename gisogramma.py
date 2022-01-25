def gis(stack):
    st1 = []
    st1.append(stack[0])
    smax = 0
    b = int(0)
    b = stack[0]
    count1 = len(st1)
    s = b * count1
    if s >= smax:
        smax = s

    count1 = 1
    for i in range(len(stack) - 1):
        a1 = stack[i + 1]
        b1 = stack[i]
        if a1 >= b1:
            st1.append(stack[0])
            count1 = len(st1)
            s = b * count1
            if s >= smax:
                smax = s

    return smax


# st = [int, input().split()]
# N = int(input())
st = [int(i) for i in '7 2 1 4 5 1 3 3'.split()]
print(gis(st))
