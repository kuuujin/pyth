import sys
input = sys.stdin.readline

submit_students = set([int(input()) for _ in range(28)])
all_students = set(range(1,31))
missing_students = all_students - submit_students
for student in sorted(missing_students):
    print(student)