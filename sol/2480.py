dice = list(map(int, input().split()))
dice.sort()

match len(set(dice)):
    case 1:
        print(10000 + dice[0] * 1000)
    case 2:
        print(1000 + dice[1] * 100)
    case 3:
        print(dice[2] * 100)