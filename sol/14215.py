tri = list(map(int,input().split()))
tri.sort()
if tri[2] < tri[0] + tri[1]:
    print(sum(tri))
else:
    print((tri[0] + tri[1]) * 2 - 1)