def Rev(x):
    return int(str(x)[::-1])
x,y = map(int,input().split())
print(Rev(Rev(x)+Rev(y)))
