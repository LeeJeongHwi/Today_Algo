from sys import stdin
from copy import deepcopy
from collections import deque
stdin = open('input.txt')
n = int(stdin.readline())

#init (처음할떄 그냥 for문으로 받아서 넣는것도 나쁘지않을듯)
# rgb_maps = [list(stdin.readline().rstrip()) for _ in range(n)]
# rrb_maps = deepcopy(rgb_maps)
# for i in range(n):
#     for j in range(n):
#         if rrb_maps[i][j] == "G":
#             rrb_maps[i][j] = "R"

rgb_maps = []
rrb_maps = []

for i in range(n):
    line = stdin.readline().rstrip()
    rgb_maps.append(list(line))
    rrb_maps.append(list(line.replace("G","R")))

rgb_visit = [[0 for _ in range(n)] for _ in range(n)]
rrb_visit = [[0 for _ in range(n)] for _ in range(n)]

#bfs
def bfs(y,x, color, maps, visit):
    q = deque()
    q.append([y,x])
    visit[y][x] = 1
    while q:
        n_y, n_x = q.popleft()

        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = n_y + dy
            nx = n_x + dx

            if 0 <= ny < n and 0 <= nx < n:
                if visit[ny][nx] == 0 and maps[ny][nx] == color:
                    visit[ny][nx] = 1
                    q.append([ny,nx])


rgb_count = 0
rrb_count = 0

for i in range(n):
    for j in range(n):
        if rgb_visit[i][j] == 0:
            bfs(i, j, rgb_maps[i][j], rgb_maps, rgb_visit)
            rgb_count += 1

for i in range(n):
    for j in range(n):
        if rrb_visit[i][j] == 0:
            bfs(i, j, rrb_maps[i][j], rrb_maps, rrb_visit)
            rrb_count += 1


print(rgb_count, rrb_count)