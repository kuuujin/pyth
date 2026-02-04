import sys
input = sys.stdin.readline

N = int(input())
exam = list(map(int, input().split()))
B, C = map(int, input().split())

tot = 0

for students in exam:
    tot += 1
    students -= B

    if students > 0:
        tot += (students + C - 1) // C

print(tot)