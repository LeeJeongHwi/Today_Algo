from sys import stdin
from collections import deque

# 효율이 너무 떨어져서 다시한번 ..해봐야함

stdin = open('input.txt')
n, m = map(int,stdin.readline().split())
tom = [list(map(int,stdin.readline().split())) for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]
q = deque()
for i in range(m):
    for j in range(n):
        if tom[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            q.append([i,j])
        elif tom[i][j] == -1:
            visit[i][j] = -1

def bfs():
    dayz = 0
    while q:
        ny, nx = q.popleft()

        # 1 Simulation
        if 0 <= ny + 1 < m and 0 <= nx < n:
            if visit[ny+1][nx] == 0 and tom[ny+1][nx] ==0:
                q.append([ny+1, nx])
                visit[ny+1][nx] = visit[ny][nx] + 1
                dayz = visit[ny][nx] + 1

        if 0 <= ny - 1 < m and 0 <= nx < n:
            if visit[ny-1][nx] == 0 and tom[ny-1][nx] ==0:
                q.append([ny-1, nx])
                visit[ny-1][nx] = visit[ny][nx] + 1
                dayz = visit[ny][nx] + 1

        if 0 <= ny < m and 0 <= nx + 1 < n:
            if visit[ny][nx+1] == 0 and tom[ny][nx+1] ==0:
                q.append([ny, nx+1])
                visit[ny][nx+1] = visit[ny][nx] + 1
                dayz = visit[ny][nx] + 1

        if 0 <= ny < m and 0 <= nx - 1 < n:
            if visit[ny][nx-1] == 0 and tom[ny][nx-1] ==0:
                q.append([ny, nx-1])
                visit[ny][nx-1] = visit[ny][nx] + 1
                dayz = visit[ny][nx] + 1

    for i in range(m):
        for j in range(n):
            if visit[i][j] == 0:
                print(-1)
                return
    
    if dayz == 0:
        print(dayz)
    else:
        print(dayz-1)
    
bfs()
