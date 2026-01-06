import math
n = int(input())
shirts = list(map(int,input().split()))
t,p = map(int,input().split())

shirts = list(map(lambda x: math.ceil(x/t),shirts))
print(sum(shirts))
a,b = divmod(n,p)
print(a,b)