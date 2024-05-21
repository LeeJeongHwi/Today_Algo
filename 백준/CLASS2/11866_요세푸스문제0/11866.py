from sys import stdin
from collections import deque
stdin = open('input.txt')

n, k = map(int,stdin.readline().split())

ans = []

q = deque([str(x) for x in range(1,n+1)])

count = 1
while q:
    if count == k:
        count = 1
        ans.append(q.popleft())
        continue
    q.rotate(-1)
    count+=1

print("<",end="");print(", ".join(ans),end="");print(">",end="")