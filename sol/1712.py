import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
n = 0
if b>=c: n = -1
else: n = a // (c-b) + 1
print(n)