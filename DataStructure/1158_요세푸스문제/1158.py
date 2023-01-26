from sys import stdin
from collections import deque
stdin = open("input.txt","r")

n,k = map(int,stdin.readline().split())

q = deque([x+1 for x in range(n)])
ans = []
count = 1
while q:
    if count != k:
        count+=1
        q.append(q.popleft())
        continue
    ans.append(str(q.popleft()))
    count = 1

print("<",end="")
print(", ".join(ans),end="")
print(">")