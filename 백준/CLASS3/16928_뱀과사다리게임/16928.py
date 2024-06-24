from sys import stdin
from collections import deque
stdin = open('input.txt')
N, M = map(int,stdin.readline().split())
ladders = {}
snakes = {}
visit = [float("inf") for _ in range(101)]

for _ in range(N):
    x,y = map(int,stdin.readline().split())
    ladders[x] = y

for _ in range(M):
    u,v = map(int,stdin.readline().split())
    snakes[u] = v 

# Ladders 랑 Snakes를 하나만 둬도 됐었음 (중복이 안되니까)

# print(ladders,snakes)
def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 0

    while q:
        now = q.popleft()

        # print(now, visit[now])
        if now == 100:
            return visit[now]
        for nd in [1,2,3,4,5,6]:
            next = now + nd
            if next <= 100:
                if next in ladders:
                    if visit[now]+1 < visit[ladders[next]]:
                        q.append(ladders[next])
                        visit[ladders[next]] = visit[now] + 1
                elif next in snakes:
                    if visit[now]+1 < visit[snakes[next]]:
                        q.append(snakes[next])
                        visit[snakes[next]] = visit[now] + 1
                else:
                    if visit[now]+1 < visit[next]:
                        q.append(next)
                        visit[next] = visit[now] + 1

print(bfs(1))
