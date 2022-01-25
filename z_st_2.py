n = int(input())

A = []
Mn = set()
for i in range(n):
    Mi = int(input())
    row = ['']*Mi
    for j in range(Mi):
        row[j] = input()
        Mn.add(row[j])
    A.append(row)
    t = {i for i in row}


for i in range(len(A)):
    print(A[i])

print(Mn)



# for i in range(0, n):
#     Mi = int(input())
#     m[i].
#     for j in range(0, Mi):
#         m[i][j] = input()
