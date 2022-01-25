def scnt(stack):
    s = sum(stack) * len(stack)
    return s


def gis(stack):
    st.append(stack[0])
    s = st[0]
    smax = s
    for i in range(1, len(stack)-1):
        if stack[i] >= st[0]:
            st.append(stack[i])
            s = scnt(st)
            smax = max(smax, s)
        if stack[i] < st[0]:
            st=[]
            print(i)
            st.append(stack[i])
            s = scnt(st)
            smax = max(smax, s)
    return smax


st = [int(i) for i in '7 2 1 4 5 1 3 3'.split()]
# print(scnt(st))
print(gis(st))
