L = int(input())
text: str = input()
H: int = 0

for i in range(L):
    asc = ord(text[i]) - 96
    H += asc * (31 ** i)

print(H%1234567891)