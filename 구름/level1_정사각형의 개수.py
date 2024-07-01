# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 1
for i in range(2,N+1):
	dp[i] = dp[i-1] + (i**2)
	
print(dp[N])