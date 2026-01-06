import sys
from collections import Counter

input = sys.stdin.readline

a = input().strip()
b = input().strip()

cnt1 = Counter(a)
cnt2 = Counter(b)

result = (cnt1 - cnt2) + (cnt2 - cnt1)
print(sum(result.values()))