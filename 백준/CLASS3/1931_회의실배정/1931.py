"""
그리디 알고리즘이라 우선은 빨리 끝나는 것으로 정렬해야한다
빨리 끝나는걸 정렬하고, 이전회의 끝나는 시간 <= 지금회의 시작시간을 만족하면 cnt+=1

즉 빨리 끝나는 것으로. Greedy하게
"""
from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

conf = [list(map(int,stdin.readline().split())) for _ in range(n)]

conf.sort(key=lambda x: (x[1],x[0]))

cnt = 1

now_conf = None

for i, (start, end) in enumerate(conf):
    if i == 0:
        now_conf = [start, end]
        continue

    if now_conf[1] <= start:
        now_conf = [start, end]
        cnt+=1



print(cnt)

