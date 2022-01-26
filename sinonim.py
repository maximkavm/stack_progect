n = int(input())
sdict = dict()
for i in range(n):
    k, val = map(str, input().split())
    sdict[k] = val

to_found = input()

for k, v in sdict.items():
    if to_found == v:
        print(k)
    if to_found == k:
        print(v)




