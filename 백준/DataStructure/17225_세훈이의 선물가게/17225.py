"""
DataStructure : Queue
"""

from sys import stdin
from collections import deque
stdin = open("input.txt","r")

# Blue : sang / Red : jisu
# sang : A sec / jisu : B sec
# same time : sang


"""
Input(1) : A, B, N(손님 수)
Input(~) : t(time), c(color), m(개수)
"""
num = 0

A, B, N = map(int, stdin.readline().split())

sang = deque()
jisu = deque()

sang_ans = []
jisu_ans = []

for i in range(N):
    t, c, m = stdin.readline().split()
    t = int(t)
    m = int(m)
    # Q에는 [색, 시작시간, 끝시간]으로 삽입
    for mul in range(m):
        if c == "B":
            startT = t+(A*mul)
            endT = t+(A*mul)+A
            if sang:
                if sang[-1][2] > startT: # 이미 맡아진 일보다 더 먼저 들어올 때
                    startT = sang[-1][2]
                    endT = startT+A
            sang.append([c, startT, endT])
            
        else:
            startT = t+(B*mul)
            endT = t+(B*mul)+B
            if jisu:
                if jisu[-1][2] > startT: # 이미 맡아진 일보다 더 먼저 들어올 때
                    startT = sang[-1][2]
                    endT = startT+B
            jisu.append([c, startT, endT])

count = 0
while (sang or jisu):

    count+=1
    if sang and (not jisu):
        sang.popleft()
        sang_ans.append(str(count))
        continue
    elif (not sang) and jisu:
        jisu.popleft()
        jisu_ans.append(str(count))
        continue

    if sang[0][1] > jisu[0][1]:
        jisu.popleft()
        jisu_ans.append(str(count))
    else: # 같을때도 포함
        sang.popleft()
        sang_ans.append(str(count))
    
print(len(sang_ans))
print(" ".join(sang_ans))
print(len(jisu_ans))
print(" ".join(jisu_ans))