from sys import stdin
from collections import deque
stdin = open('input.txt')

N, M, T = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(N)]
memo = [[0 for _ in range(M)] for _ in range(N)]

def bfs(start):
    start_x, start_y = start
    q = deque()
    q.append([start_y, start_x, False])
    memo[start_y][start_x] = 0
    dists = float("inf")
    gram_dists = float("inf")
    while q:
        y, x, gram = q.popleft()
        if y == N-1 and x == M-1: # 가장 먼저 공주 찾은 케이스
            dists = min(dists, memo[y][x])
            break
        
        for i, [dy, dx] in enumerate([[0,1],[1,0],[-1,0],[0,-1]]):
            ny = dy + y
            nx = dx + x
            if ny == 0 and nx == 0:
                continue

            if 0 <= ny < N and 0 <= nx < M :
                if maps[ny][nx] == 0 and memo[ny][nx] == 0: # 길 이동
                    q.append([ny, nx, gram])
                    memo[ny][nx] = memo[y][x] + 1

                elif maps[ny][nx] == 2 and memo[ny][nx] == 0: # 그람 획득
                    # 현재 그람과 공주와의 거리 계산
                    gram_dists = min(gram_dists, (abs(ny - (N-1)) + abs(nx - (M-1))) + memo[y][x] + 1)
                    # print(abs(ny - (N-1)), abs(nx - (M-1)), memo[y][x] + 1)
    
    # print(dists, gram_dists)
    return min(dists, gram_dists)

time = bfs([0, 0])

if time <= T:
    print(time)
else:
    print("Fail")
