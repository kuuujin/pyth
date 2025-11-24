cnt = 0
vowel = [ord('a'),ord('e'),ord('i'),ord('o'),ord('u')]
s = input()
for char in s:
    if ord(char) in vowel:
        cnt += 1
print(cnt)