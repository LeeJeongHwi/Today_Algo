from sys import stdin
from itertools import permutations
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

nlist = list(map(int,stdin.readline().split()))
nlist.sort()

for comb in permutations(nlist, m):
    for c in comb:
        print(c,end=" ")
    print()