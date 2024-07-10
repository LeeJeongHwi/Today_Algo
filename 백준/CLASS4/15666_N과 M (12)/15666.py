from sys import stdin
from itertools import product
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())
nlist = list(map(int,stdin.readline().split()))
visit = [False for _ in range(n)]
nlist.sort()

ans = []
def back(count, num_list):
    if count == m: # 조건 만족
        ans.append(tuple(num_list))
        return

    for i in range(n):
        if num_list:
            if num_list[-1] > nlist[i]:
                continue
        visit[i] = True
        num_list.append(nlist[i])
        back(count+1,num_list)
        visit[i] = False
        num_list.pop()

back(0, [])
for a in dict.fromkeys(ans):
    print(*a)