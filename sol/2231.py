import sys
input = sys.stdin.readline

n = int(input())
start = max(1, n - (len(str(n)) * 9))
answer = 0

for i in range(start, n):
    de_sum = i + sum(map(int, str(i)))
    if de_sum == n:
        answer = i
        break
print(answer)