tot = 0
for _ in range(5):
    score = int(input())
    if score < 40: score = 40
    tot += score
print(tot//5)