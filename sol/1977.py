import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

squares = []

i = int(m ** 0.5) 
if i * i < m: 
    i += 1

while i * i <= n:
    squares.append(i * i)
    i += 1

if squares:
    print(sum(squares)) 
    print(squares[0])   
else:
    print(-1)