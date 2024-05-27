from sys import stdin
from collections import Counter
stdin = open('input.txt')

n = int(stdin.readline())

nlist = [int(stdin.readline()) for _ in range(n)]
nlist.sort()

def get_Mode(n_count):
    n_count.sort(key=lambda x:(-x[1],x[0]))
    max_count = n_count[0][1] # 가장 최빈값 값
    mlist = []
    for m, count in n_count:
        if count == max_count:
            mlist.append([m, count])
        else: # 가장 최빈값 위주로 정렬되었기 때문
            break
    
    # print(mlist) # Sort 된 상태이므로 [1]번째가 2번째가 작은 수이다.
    if len(mlist) > 1:
        return mlist[1]
    else:
        return mlist[0]
    

n_count = list(Counter(nlist).items())
mode, _ = get_Mode(n_count)

mean = round(sum(nlist)/n,0)
mid = nlist[n//2]

ranges = nlist[-1] - nlist[0]

print(int(mean))
print(mid)
print(mode)
print(ranges)
