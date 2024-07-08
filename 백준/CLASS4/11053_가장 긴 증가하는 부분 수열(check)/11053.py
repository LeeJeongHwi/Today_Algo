from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
nlist = list(map(int,stdin.readline().split()))

dp = [1 for _ in range(n)]

# Longest Increasing Subsequence
# 꼭 다시 한번 풀어보기

for i in range(n):
    for j in range(i):
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
