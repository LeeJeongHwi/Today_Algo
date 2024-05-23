from sys import stdin
from collections import Counter
stdin = open('input.txt')

n = int(stdin.readline())

numlist = list(map(int,stdin.readline().split()))
num_count = Counter(numlist)

m = int(stdin.readline())
mlist = list(map(int,stdin.readline().split()))

ans = []

for snum in mlist:
    if snum not in num_count:
        ans.append("0")
    else:
        ans.append(str(num_count[snum]))

print(" ".join(ans))