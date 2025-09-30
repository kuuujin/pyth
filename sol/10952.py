while(True):
    try:
        a,b = map(int,input().split())
        if a==0 and b ==0: break
    except:
        break
    print(a+b)