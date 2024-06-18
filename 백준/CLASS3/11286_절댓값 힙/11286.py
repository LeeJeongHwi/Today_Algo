from sys import stdin
import heapq
stdin = open('input.txt')
n = int(stdin.readline())

hp = []

def items(v):
    return (abs(v), v)

for _ in range(n):
    v = int(stdin.readline())

    if v == 0:
        if hp:
            print(heapq.heappop(hp)[1])
            continue
        else:
            print(0)
            continue

    heapq.heappush(hp, items(v))