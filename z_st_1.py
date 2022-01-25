n = [int(i) for i in input().split()]
a = set(n)
n1 = [int(i) for i in input().split()]
a1 = set(n1)
print(len(a)-len(a.difference(a1)))