l,p = map(int,input().split())
tot = l*p
lst = list(map(int,input().split()))
result = list(map(lambda x: x-tot,lst))
print(*result)