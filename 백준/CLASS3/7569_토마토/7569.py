from pprint import pprint
from sys import stdin
from collections import deque
stdin = open('input.txt')
n, m, h = map(int,stdin.readline().split())
tomato = [[list(map(int,stdin.readline().split())) for _ in range(m)] for _ in range(h)]
visit = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(h)]

q = deque()

def bfs():
    # 6 direct
    """
    ceil : 1 0 0 (h+1)  | floor : -1 0 0 (h-1)
    Left : 0 0 -1 (x-1) | Up : 0 1 0 (y+1)
    right : 0 0 1 (x+1) | Down : 0 -1 0 (y-1)
    """
    direct = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
    dayz = 0

    while q:
        now_z, now_y, now_x = q.popleft()
        
        for dz,dy,dx in direct:
            nz = now_z + dz
            ny = now_y + dy
            nx = now_x + dx

            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n:
                if visit[nz][ny][nx] == 0 and tomato[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = visit[now_z][now_y][now_x] + 1
                    q.append([nz,ny,nx])
                    # 이게 오래걸릴 수 있음
                    dayz = max(dayz, visit[nz][ny][nx]) 
      
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if visit[i][j][k] == 0:
                    print(-1)
                    return

    if dayz == 0:
        print(0)
        return
    else:
        print(dayz-1)

for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 1 and visit[i][j][k] == 0:
                q.append([i,j,k])
                visit[i][j][k] = 1
            if tomato[i][j][k] == -1:
                visit[i][j][k] = -1

bfs()