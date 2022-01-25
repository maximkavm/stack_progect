def psfstr(stack):
    st = []
    for i in range(len(stack)):
        if stack[i].isnumeric():
            st.append(stack[i])
        if stack[i] == '+':
            a = int(st.pop())
            b = int(st.pop())
            st.append(a + b)
        if stack[i] == '-':
            a = int(st.pop())
            b = int(st.pop())
            st.append(b - a)
        if stack[i] == '*':
            a = int(st.pop())
            b = int(st.pop())
            st.append(a * b)
    return st[0]


#str1 = '7 2 3 * -'
str1 = input()
print(psfstr(str1.split()))
