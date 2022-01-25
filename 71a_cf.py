N = int(input())
mst = []
for i in range(0, N):
    str1 = input()
    if len(str1) > 10:
        mst.append(str1[0] + str(len(str1)-2) + str1[-1])
    else:
        mst.append(str1)

for i in range(0, N):
    print(mst[i])
