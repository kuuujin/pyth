import sys
input = sys.stdin.readline

xpoint,ypoint = [],[]
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    xpoint.append(x)
    ypoint.append(y)

min_x = min(xpoint)
max_x = max(xpoint)
min_y = min(ypoint)
max_y = max(ypoint)

w = max_x - min_x
h = max_y - min_y
print(w*h)