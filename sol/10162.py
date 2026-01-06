import sys
input = sys.stdin.readline

TIME_A = 300
TIME_B = 60
TIME_C = 10

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    count_a, T = divmod(T, TIME_A) 
    count_b, T = divmod(T, TIME_B) 
    count_c, T = divmod(T, TIME_C)
    
print(count_a, count_b, count_c)