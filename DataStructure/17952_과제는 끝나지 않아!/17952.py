"""
DataStructure : Stack
"""
from sys import stdin
from collections import deque
stdin = open("input.txt","r")

N = int(stdin.readline())

q = deque()

minute = 0
score = 0

for _ in range(N):
    l = stdin.readline().split()
    # print(q, l)
    minute+=1

    if int(l[0]) == 1:
        q.append([int(l[1]), int(l[2])])

    if q:
        q[-1][1] -= 1
        if q[-1][1] == 0:
            score += q[-1][0]
            q.pop()
    

print(score)


    


