from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

RGB = [[0,0,0]]+[list(map(int,stdin.readline().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n+1)]
# 2차원 dp 배열이 핵심임, 해당 좌표에 대한 최솟값이어야함

for i in range(1,n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]

print(min(dp[n]))