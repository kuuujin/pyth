import sys
input = sys.stdin.readline

current_people = 0
max_people = 0

for _ in range(4):
    out_n, in_n = map(int, input().split())
    current_people = current_people - out_n + in_n
    max_people = max(max_people, current_people)

print(max_people)