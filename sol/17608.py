import sys
input = sys.stdin.readline
sticks: list[int] = []

N = int(input())
for _ in range(N):
    h = int(input())
    sticks.append(h)
max_h: int = 0
count: int = 0

for stick in reversed(sticks):
    if stick > max_h:
        count += 1
        max_h = stick
            
print(count)
