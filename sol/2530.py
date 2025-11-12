h,m,s = map(int,input().split())
d = int(input())
a,b =divmod(d,60)
m += a
s += b
if s>=60:
    m +=1
    s -=60
if m>=60:
    i,j = divmod(m,60)
    h +=i
    m = j
h = h %24

print(h,m,s)