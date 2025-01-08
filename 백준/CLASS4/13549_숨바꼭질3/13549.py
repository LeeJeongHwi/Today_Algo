from sys import stdin
from collections import deque
stdin = open('input.txt')

N, K = map(int,stdin.readline().split())

# 걷기 : x-1, x+1 (1초)
# 순간이동 : 2*x (0초)

def solution(N, K):
    maps = [-1 for _ in range(100001)]
    q = deque()
    q.append(N)
    maps[N] = 0 # init
    while q:
        now = q.popleft()
        if now == K:
            print(maps[:K+1])
            return maps[now]
        for i, d_p in enumerate([2, -1, 1]):
            if i != 0:
                next_p = now + d_p
                if 0 <= next_p <= 100000: # 범위 췤!
                    if maps[next_p] == -1: # -1이 아니라는건 이미 지나갔다는 것, 1초를 추가하는 것이기 때문
                        q.append(next_p)
                        maps[next_p] = maps[now] + 1

            elif i == 0:
                next_p = now * d_p
                if 0 <= next_p <= 100000:
                    if maps[next_p] > maps[now] or maps[next_p] == -1: # 얘는 기존보다 빠를 수 있음
                        q.append(next_p)
                        maps[next_p] = maps[now]


print(solution(N,K))

# 여기서의 핵심은 2 -1 1순으로 가는게 제일 핵심이다
# 2는 0초니까 당연히 최소값이므로 이게 가장 빠르기 때문
# 중요 : 0-1 BFS도 찾아보자