angles = []
for _ in range(3):
    angles.append(int(input()))
tot = sum(angles)
unique = len(set(angles))
if tot != 180:
    print('Error')
elif unique == 1:
    print('Equilateral')
elif unique == 2:
    print('Isosceles')
else: print('Scalene')