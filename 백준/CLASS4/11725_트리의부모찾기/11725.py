from sys import stdin
from collections import deque
stdin = open('input.txt')
n = int(stdin.readline())

tree = {i:[] for i in range(1,n+1)}
visit = [0 for _ in range(n+1)]

for _ in range(n-1):
    A, B = map(int,stdin.readline().split())
    tree[A].append(B)
    tree[B].append(A)

q = deque()
visit[1] = 1
q.append([1,1])
while q:
    prev, now = q.popleft()
    for next_node in tree[now]:
        if visit[next_node] == 0:
            visit[next_node] = now
            q.append([now, next_node])

print("\n".join(map(str,visit[2:])))