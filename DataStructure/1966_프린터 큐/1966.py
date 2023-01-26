from sys import stdin
from collections import deque

stdin = open("input.txt","r")

case = int(stdin.readline())

for _ in range(case):
    
    n, t_n = map(int,stdin.readline().split())
    q = deque([(x,prior) for x,prior in enumerate(list(map(int,stdin.readline().split())))])

    count = 0
    while 1:
        x,p = q.popleft()
        flag = True
        for _, pr in q:
            if pr > p: # 대기열에 있는 우선순위가 더 클 때
                flag = False
                break
        
        if not flag:
            q.append((x,p))
            continue
        else: # 현재 우선순위가 가장 크다는 것
            if x == t_n:
                count+=1
                print(count)
                break
            count+=1