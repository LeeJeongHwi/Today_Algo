from sys import stdin
from itertools import combinations
stdin = open('input.txt')
n = int(stdin.readline())

tangs = list(map(int,stdin.readline().split()))

left = 0; right = 0; max_cnt = -1
# kind가 
nums = {x:0 for x in range(1,11)}
cnt = 0
kind = 0
while right < n:
    if nums[tangs[right]] == 0:
        kind += 1

    cnt += 1
    nums[tangs[right]] += 1

    if kind > 2:
        nums[tangs[left]] -= 1
        if nums[tangs[left]] == 0:
            kind -= 1
        cnt -=1
        left += 1
    
    right += 1
    max_cnt = max(max_cnt, cnt)
    # print(left, right, kind, cnt)

print(max_cnt)