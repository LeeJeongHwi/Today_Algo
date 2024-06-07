from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())

import heapq

numlist = []

for _ in range(n):
    num = int(stdin.readline())
    if not numlist:
        if num == 0:
            print(0)
            continue
        heapq.heappush(numlist, num)

    else:
        if num == 0:
            print(heapq.heappop(numlist))
        else:
            heapq.heappush(numlist, num)
            # heapq.heapify(numlist)