from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    mp = deque(input().split())
    vp = deque()
    for i in range(K):
        vp.append(int(mp[i]))
    print(min(vp))
    for i in range(K, N):
        vp.popleft()
        vp.append(int(mp[i]))
        print(min(vp))
