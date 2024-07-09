from sys import stdin
from itertools import product
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())
nlist = list(map(int,stdin.readline().split()))
visit = [False for _ in range(n)]
nlist.sort()

ans = []
def back(count):
    if count == m:
        prev = None
        for i,v in enumerate(ans):
            if i == 0:
                prev = ans[i]
                continue
            if prev <= ans[i]:
                continue
            else:
                return
            
        print(' '.join(map(str,ans)))
        return
    
    for i in range(n):
        if ans:
            if ans[-1] <= nlist[i]:
                pass
        ans.append(nlist[i])
        visit[i] = True
        back(count+1)
        visit[i] = False
        ans.pop()

back(0)

