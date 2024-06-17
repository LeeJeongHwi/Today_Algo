from sys import stdin
from collections import deque
from pprint import pprint
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())


maps = [[int(x) for x in stdin.readline().rstrip()] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    while q:
        now_y, now_x = q.popleft()
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny = now_y + dy
            nx = now_x + dx
            if  0 <= ny < n and 0 <= nx < m:
                if visit[ny][nx] == 0 and maps[ny][nx] == 1:
                    q.append([ny, nx])
                    visit[ny][nx] = visit[now_y][now_x] + 1

bfs(0,0)
print(visit[n-1][m-1])