import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
names = [input()[0] for _ in range(N)]

cnt = Counter(names)

result = [k for k, v in cnt.items() if v >= 5]

if not result:
    print("PREDAJA")
else:
    print("".join(sorted(result)))