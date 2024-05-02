from sys import stdin
from collections import deque
stdin = open("input.txt","r")

n = int(stdin.readline())

q = deque()
for _ in range(n):
    line = stdin.readline().split()
    
    if line[0] == "push":
        q.append(line[1])
    elif line[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)            
    elif line[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif line[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif line[0] == "size":
        print(len(q))