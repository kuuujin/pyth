counts = [0]*26
a = ord('a')
s = input()
for char in s:
    counts[ord(char)-a] += 1
print(*counts)