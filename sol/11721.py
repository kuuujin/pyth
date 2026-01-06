import sys

input = sys.stdin.readline

word = input().rstrip("\n")
a,b = divmod(len(word),10)
for i in range(a+1):
    print(word[i*10:i*10+10])