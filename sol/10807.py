cnt = int(input())
nums = list(map(int,input().split()))
target = int(input())
count = 0
for i in range(cnt):
    if nums[i] == target:
        count += 1
print(count)