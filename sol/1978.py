import sys
input = sys.stdin.readline

max_num = 1000
is_prime = [True] * (max_num + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(max_num**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, max_num+1, i):
            is_prime[j]=False

N = int(input())
numbers = list(map(int,input().split()))
cnt = 0
for num in numbers:
    if is_prime[num]:
        cnt += 1

print(cnt)