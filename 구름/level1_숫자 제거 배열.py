# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin

N, K = stdin.readline().split()
N = int(N)
num_list = list(stdin.readline().split())

ans = 0
for num in num_list:
		if K in num:
			continue
		ans+=1

print(ans)



