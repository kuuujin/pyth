n,x = map(int,input().split())
a = list(map(int,input().split()))
arr = []
for i in range(n):
    if a[i] < x:
        arr.append(a[i])
print(*arr)