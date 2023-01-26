from sys import stdin
from collections import deque

stdin = open("input.txt","r")

n = int(stdin.readline())

q = deque([x+1 for x in range(n)])

minus = 0
while (n-minus)>1:
    q.popleft()
    q.append(q.popleft())
    minus += 1

print(q[0])
