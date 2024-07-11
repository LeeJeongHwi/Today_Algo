from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

# Input
triangle = [list(map(int,stdin.readline().split())) for _ in range(n)]

# DP
dp = [[0]*i for i in range(1,n+1)]

dp[0][0] = triangle[0][0] # 꼭대기
for i in range(1,n):
    for j in range(i+1):
        if j == 0: # 맨 왼쪽
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i: # 맨 오른쪽
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else: # 그 외
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]

print(max(dp[n-1]))
