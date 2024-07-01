# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin
from collections import Counter
N,K = map(int, stdin.readline().split())

num_list = list(map(int,stdin.readline().split()))

ans = []

for num in num_list:
	ten_to_bin = str(bin(num))
	ans.append([Counter(ten_to_bin)["1"], num])

ans.sort(key=lambda x:(-x[0],-x[1]))
print(ans[K-1][1])