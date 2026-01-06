import sys
input = sys.stdin.readline

n = int(input())

cnt = 1 
range_end = 1 

while n > range_end:
    range_end += 6 * cnt
    cnt += 1

print(cnt)