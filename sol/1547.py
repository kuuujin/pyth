import sys
input = sys.stdin.readline

lst = [1,0,0]
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    lst[y-1], lst[x-1] = lst[x-1], lst[y-1]
print(lst.index(1)+1)