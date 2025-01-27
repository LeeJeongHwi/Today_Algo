from sys import stdin
from itertools import combinations
stdin = open('input.txt')


n, m = map(int,stdin.readline().split())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

chicken = []
home = []
len_home = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chicken.append([i, j])
        elif maps[i][j] == 1:
            len_home += 1
            home.append([i, j])

combs = combinations(chicken, m)

def dist(home, chick):
    dists = [float("inf") for _ in range(len_home)]
    # 해당 집이 위 치킨집에서 가장 가까운 것을 저장
    # 선택된 집이 치킨집과의 거리를 계산
    for i, h in enumerate(home):
        # dist clac
        for ch in chick:
            dists[i] = min(dists[i], abs(h[0]-ch[0]) + abs(h[1]-ch[1]))
    return sum(dists)

min_dist = float("inf")
for comb in combs:
    min_dist = min(dist(home, comb), min_dist)

print(min_dist)