num = map(int, input().split())
print(sum(x**2 for x in num) % 10)