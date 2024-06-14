from sys import stdin
from collections import deque

stdin = open('input.txt')
n, k = map(int,stdin.readline().split())

# 위치가 X일때 1초후에 X-1, X+1로 이동 / 순간이동시 2*X

visit = [0 for _ in range(100001)]

def search(start, target):
    global visit

    q = deque([start])
    visit[start] = 1

    if start == target:
        return 0

    while q:
        now = q.popleft() # 현재 위치
        for dx in [-1, 1, now]:
            nx = now + dx
            if nx < 0 or nx > 100000:
                continue

            if visit[nx] == 0:
                if nx == target:
                    return visit[now]

                q.append(nx)                
                visit[nx] = visit[now] + 1


print(search(n, k))

