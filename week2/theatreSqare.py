from math import ceil

m,n,a = input().split()

m = int(m)
n = int(n)
a = int(a)

print(ceil(n/a)*ceil(m/a))