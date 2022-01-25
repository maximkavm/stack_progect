def skran(stack):
    st = []
    for i in range(len(stack)):
        if stack[i] == '{' or stack[i] == '[' or stack[i] == '(':
            st.append(stack[i])
        if (stack[i] == ']') or stack[i] == '}' or stack[i] == ')':
            if (len(st) != 0) and (st[len(st) - 1] == '[' or st[len(st) - 1] == '{' or st[len(st) - 1] == '('):
                st.pop()
        else:
            if (stack[i] == '}' or stack[i] == ']' or stack[i] == ')'):
                st.append(stack[i])
    if len(st) == 0:
        return 'yes'
    else:
        return 'no'


# str1 = input()
str1 = '[[(]]'
print(skran(str1))
