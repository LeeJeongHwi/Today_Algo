from sys import stdin
from itertools import combinations_with_replacement
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

nlist = [i for i in range(1,n+1)]

for comb in combinations_with_replacement(nlist,m):
    for c in comb:
        print(c, end=" ")
    print()