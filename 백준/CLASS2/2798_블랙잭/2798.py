from itertools import combinations
from sys import stdin

stdin = open("input.txt","r")

N, M = map(int,stdin.readline().split())

cards = list(map(int,stdin.readline().split()))

max_sum = 0
for combs in combinations(cards,3):
    sum_combs = sum(combs)
    if M-sum_combs < 0:
        continue
    max_sum = max(sum_combs,max_sum)

print(max_sum)
    
"""
여기서 cards 자체를 내림차순으로 정렬하고
3중 for문으로 최댓값부터 계산해오면 더 빠르게 탐색이 가능함
"""