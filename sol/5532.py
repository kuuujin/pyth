import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
days_kor = math.ceil(a/c)
days_math = math.ceil(b/d)
days = max(days_kor,days_math)
print(l-days)