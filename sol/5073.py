import sys
input = sys.stdin.readline

while True:
    sides = list(map(int, input().split()))

    if sum(sides) == 0:
        break
        
    sides.sort()
    
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif len(set(sides)) == 1:
        print("Equilateral")
    elif len(set(sides)) == 2:
        print("Isosceles")
    else:
        print("Scalene")