import sys
input = sys.stdin.readline

n = int(input())
f = int(input())
n -= n % 100
a = n % f
if a == 0: print("00")
else: print(f"{f-a:02d}")