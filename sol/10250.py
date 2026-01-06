import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = (N - 1) % H + 1
    room_num = (N - 1) // H + 1
    
    print(f"{floor}{room_num:02d}")