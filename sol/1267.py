import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
sumY = 0
sumM = 0
for time in lst:
    sumY += ((time//30)+1) * 10
    sumM += ((time//60)+1) * 15
if(sumM < sumY): print("M",sumM)
elif(sumM > sumY): print("Y", sumY)
else: print("Y M",sumM)
