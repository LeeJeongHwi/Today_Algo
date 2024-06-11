from sys import stdin
from collections import deque

stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

nodes = {x:[] for x in range(1,n+1)}
visit = [False for _ in range(0,n+1)]

for _ in range(m):
    x, y = map(int,stdin.readline().split())
    
    nodes[x].append(y)
    nodes[y].append(x)


def bfs(node):
    global visit
    q = deque([node])
    visit[node] = True

    while q:
        now = q.popleft()
        if now in nodes:
            for next in nodes[now]:
                if not visit[next]:
                    q.append(next)
                    visit[next] = True

count = 0
for i in nodes.keys():
    if not visit[i]:
        count+=1
        bfs(i)

print(count)