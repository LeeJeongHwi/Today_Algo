from sys import stdin
from itertools import permutations
stdin = open('input.txt')

n, m = map(int,stdin.readline().split())
numlist = list(map(int,stdin.readline().split()))

num_set = set()
for comb in permutations(numlist, m):
    num_set.add(comb)
num_set = sorted(list(num_set))

for x in num_set:
    print(*x)

