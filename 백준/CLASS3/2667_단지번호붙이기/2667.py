from sys import stdin
from collections import deque

stdin = open('input.txt')
n = int(stdin.readline())


maps = [[x for x in stdin.readline().rstrip()] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    cnt = 1

    while q:
        now_y, now_x = q.popleft()
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = now_y + dy
            nx = now_x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if visit[ny][nx] == 0 and maps[ny][nx] == "1":
                    q.append([ny, nx])
                    visit[ny][nx] = 1
                    cnt+=1

    return cnt



cnts = []
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0 and maps[i][j] == "1":
            cnt = bfs(i,j)
            cnts.append(cnt)
cnts.sort()
print(len(cnts),*cnts,sep="\n")