from sys import stdin
import heapq
# 다익스트라 문제
stdin = open('input.txt')
n = int(stdin.readline())
m = int(stdin.readline())

city = {x:[] for x in range(1,n+1)}
visit = [[float("inf"), i] for i in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,stdin.readline().split())
    city[start].append([cost, end])

start, end = map(int,stdin.readline().split())


def dijkstra(start, end):
    q = []
    heapq.heappush(q,(0,start))
    visit[start][0] = 0 # Dist update

    while q:
        dist, now = heapq.heappop(q)
        
        if visit[now][0] < dist:
            continue

        for cost, next in city[now]:
            cost = cost + dist

            if cost < visit[next][0]:
                visit[next][0] = cost
                visit[next][1] = next
                heapq.heappush(q,(cost, next))

    print(visit[end][0])

dijkstra(start, end)
