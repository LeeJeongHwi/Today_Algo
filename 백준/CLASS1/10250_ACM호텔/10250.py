from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
for _ in range(n):
    H, W, N = map(int,stdin.readline().split())
    count = 0
    col, row = 1, 1
    for i in range(1,N):
        col += 1
        if col%(H+1) == 0:
            col = 1
            row += 1
        
    
    print(col*100+row)