T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    aa = []
    if a%10==0: print(10)
    else:
        for j in range(1,5):
            aa.append((a**j%10))
        b = b%4-1
        print(aa[b])
