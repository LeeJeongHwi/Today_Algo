# DP 문제로 꼭 다시..비슷한걸로하자

from sys import stdin
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1] 

# 문제에서 X행, Y열 이기 때문에 [x][y] 이다.
for _ in range(m):
    x1, y1, x2, y2 = map(int,stdin.readline().split())
    res = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1]
    print(res)