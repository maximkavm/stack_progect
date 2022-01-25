def com_stack(*args):
    if str1 == 'push':
        stack.append(n)
        print('ok')
    elif str1 == 'pop':
        a1 = stack.pop()
        print(a1[0])
    elif str1 == 'back':
        a1 = stack[-1:]
        print(a1[0][0])
    elif str1 == 'size':
        print(len(stack))
    elif str1 == 'clear':
        stack.clear()
        print('ok')
    elif str1 == 'exit':
        print('bye')


if __name__ == '__main__':
    stack = []
    str1, *n = input().split()
    com_stack(str1, stack, n)
    while str1 != 'exit':
        str1, *n = input().split()
        com_stack(str1, stack, n)