from sys import stdin
# 재귀로풀면 시간초과가 난다
stdin = open('input.txt')

k, n = map(int,stdin.readline().split())

lans = [int(stdin.readline()) for _ in range(k)]

min_lans = 1
max_lans = max(lans)
mid = (min_lans + max_lans) // 2

while min_lans <= max_lans:
    k_n = 0
    for lan in lans:
        k_n += (lan//mid)

    if k_n >= n:
        min_lans = mid+1
        mid = (min_lans + max_lans) // 2
    else:
        max_lans = mid-1
        mid = (min_lans + max_lans) // 2

print(mid)