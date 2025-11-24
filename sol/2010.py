import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for _ in range(n):
    a = int(input())
    sum += a
print(sum-n+1)