from sys import stdin
import heapq

stdin = open('input.txt')
n = int(stdin.readline())

hq = []

for _ in range(n):
    x = int(stdin.readline())
    if not hq:
        if x == 0:
            print(0)
            continue
        else:
            heapq.heappush(hq, -x)
            continue
    
    if x == 0:
        print(abs(heapq.heappop(hq)))
    else:
        heapq.heappush(hq, -x)
