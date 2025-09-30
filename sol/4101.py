while True:
    a,b = map(int, input().split())
    if(a != 0 and b != 0):
        print("Yes") if a > b else print("No")
    else:
        exit()