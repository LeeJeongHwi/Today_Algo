# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin

# Greedy
N = int(stdin.readline())

schedules = [list(map(int,stdin.readline().split())) for _ in range(N)]

schedules.sort(key=lambda x:x[1])

count = 0
prev_end = 0
for start, end in schedules:
		if start > prev_end: # start >= prev_end -> count +=1
			prev_end = end
			count += 1
print(count)