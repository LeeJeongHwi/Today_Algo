from sys import stdin
from collections import deque
stdin = open('input.txt')
t = int(stdin.readline())
def get_Cabbage():
    m, n, num = map(int,stdin.readline().split())

    field = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]

    q = deque()

    for _ in range(num):
        px, py = map(int,stdin.readline().split())
        field[py][px] = 1


    def bfs(m, n):
        nonlocal visit, q
        while q:
            now_y, now_x = q.popleft()
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx = now_x + dx
                ny = now_y + dy
                if (0 <= ny <= n-1) and (0 <= nx <= m-1):
                    if visit[ny][nx] == 0 and field[ny][nx] == 1:
                        q.append([ny,nx])
                        visit[ny][nx] = 1

    count = 0
    for i in range(n):
            for j in range(m):
                if field[i][j] == 1 and visit[i][j] == 0:
                    q.append([i,j])
                    visit[i][j] = 1
                    bfs(m,n)
                    count +=1

    return count

for _ in range(t):
    print(get_Cabbage())