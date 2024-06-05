from sys import stdin
from collections import deque

stdin = open('input.txt')

n, m, v = map(int,stdin.readline().split())
nodes = {i:[] for i in range(1001)}

for _ in range(m):
    
    start, end = map(int,stdin.readline().split())
    nodes[start].append(end)
    nodes[end].append(start)
    

for node in nodes:
    nodes[node].sort()

dfs_visit = [0 for _ in range(1001)]
dfs_ans = []
def dfs(nodes, v):
    global dfs_visit, dfs_ans
    dfs_visit[v] = 1
    dfs_ans.append(str(v))
    for next_nodes in nodes[v]:
        if dfs_visit[next_nodes] == 0:
            dfs(nodes, next_nodes)

def bfs(nodes, v):
    visit = [0 for _ in range(1001)]
    q = deque()
    q.append(v)
    visit[v] = 1
    ans = []
    while q:
        now = q.popleft()
        ans.append(str(now))
        for next_node in nodes[now]:
            if visit[next_node] == 0:
                visit[next_node] = 1
                q.append(next_node)
    
    return ans

dfs(nodes, v)
print(" ".join(dfs_ans))
print(" ".join(bfs(nodes, v)))
