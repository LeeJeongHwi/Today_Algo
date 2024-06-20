from sys import stdin
from collections import deque
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
visit = [[-1 for _ in range(m)] for _ in range(n)]

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visit[y][x] = 0

    while q:
        now_y, now_x = q.popleft()

        for dy,dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny = now_y + dy
            nx = now_x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if visit[ny][nx] == -1 and maps[ny][nx] == 1:
                    visit[ny][nx] = visit[now_y][now_x] + 1
                    q.append([ny,nx])
                elif visit[ny][nx] == -1 and maps[ny][nx] == 0:
                    visit[ny][nx] = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            bfs(i,j)
        if maps[i][j] == 0:
            visit[i][j] = 0

for v in visit:
    print(" ".join(map(str, v)))