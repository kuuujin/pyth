import sys
input = sys.stdin.readline

n, m = map(int,input().split())
basket = [i+1 for i in range(n)]
for _ in range(m):
    i,j = map(int,input().split())
    swap = reversed(basket[i-1:j])
    basket[i-1:j] = swap
print(*basket)