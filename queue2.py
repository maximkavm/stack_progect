from  collections import  deque

def com_queue(*args):
    if str1 == 'push':
        queue.append(n)
        print('ok')
    elif str1 == 'pop':
        a1 = queue.popleft()
        print(a1[0])
    elif str1 == 'front':
        print(*queue[0])
    elif str1 == 'size':
        print(len(queue))
    elif str1 == 'clear':
        queue.clear()
        print('ok')
    elif str1 == 'exit':
        print('bye')


if __name__ == '__main__':
    queue = deque()
    str1, *n = input().split()
    com_queue(str1, queue, n)
    while str1 != 'exit':
        str1, *n = input().split()
        com_queue(str1, queue, n)








