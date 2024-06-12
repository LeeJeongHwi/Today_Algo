from sys import stdin
from collections import deque
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

maps = []
visit = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    lines = stdin.readline().rstrip()
    line = []
    for l in lines:
        line.append(l)
    maps.append(line)

# 도연이는 동서남북으로 이동
def bfs(i,j):
    global visit
    cnt = 0
    q = deque([[i,j]])
    visit[i][j] = True

    while q:
        now_y, now_x = q.popleft()
        for dy,dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = dx + now_x
            ny = dy + now_y

            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] in ["O","P"] and visit[ny][nx] == False:
                    visit[ny][nx] = True
                    q.append([ny,nx])
                    if maps[ny][nx] == "P":
                        cnt+=1

    if cnt == 0:
        return "TT"
    
    return cnt
                        



for i in range(n):
    for j in range(m):
        if maps[i][j] == "I" : # 도연이 위치
            print(bfs(i,j))
            break

