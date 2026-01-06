n,m = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

for row_a, row_b in zip(A, B):
    sum_row = [a + b for a, b in zip(row_a, row_b)]
    print(*sum_row)