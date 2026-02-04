import sys
import math

input = sys.stdin.readline
N, K = map(int, input().split())

students = [[0] * 2 for _ in range(7)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[Y][S] += 1

room = 0

for i in range(1, 7):
    for j in range(2):
        room += math.ceil(students[i][j] / K)

print(room)