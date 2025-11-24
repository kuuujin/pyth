while True:
    s = input()
    if s == "END":
        break
    rs = ''.join(reversed(s))
    print(rs)