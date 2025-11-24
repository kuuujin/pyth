import sys
input = sys.stdin.readline

x,y,w,h = map(int,input().split())
minusX = w-x
minusY = h-y
print(min(x,y,minusX,minusY))