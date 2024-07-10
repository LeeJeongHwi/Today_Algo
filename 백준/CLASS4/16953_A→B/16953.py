from sys import stdin
from collections import deque
stdin = open('input.txt')
A, B = map(int,stdin.readline().split())

# 가능한 연산은 2가지
def bfs(start, target):
    visit = {}
    q = deque()
    q.append(start)
    visit[start] = 1
    
    while q:
        now = q.popleft()
        if now == target:
            return visit[now]
        
        for ev in [now*2, (now*10)+1]:
            if ev > target:
                continue
            if ev not in visit:
                visit[ev] = visit[now] + 1
                q.append(ev)
    return -1

print(bfs(A,B))