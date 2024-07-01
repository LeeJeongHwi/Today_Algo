# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# N%보다 높은 백분위, K개의 수행평가 중 하나라도 M 보다 낮거나 같다면 A+ X
# t개의 수업에서 모든 과목에서 A+인지 확인

from sys import stdin

def grade_check(l,s,n,k,m,v):
	if (s/l)*100 >= n:
		return False
	
	for score in v: #과락체크
		if score > m:
			continue
		return False
	
	return True
		
def solution(t, case):
	# l s n k m v_k
	for c in case:
		info = c
		l,s,n,k,m = info[0],info[1],info[2],info[3],info[4]
		
		v = [info[i] for i in range(5,5+k)]
		if not grade_check(l,s,n,k,m,v):
			return 0
		
	return 1
