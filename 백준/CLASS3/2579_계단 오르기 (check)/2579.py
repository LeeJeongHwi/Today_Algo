from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

stairs = [0] + [int(stdin.readline()) for _ in range(n)]

memo = [0] + [0 for _ in range(n)]

for i in range(1,n+1):
    if i == 1:
        memo[i] = stairs[i]
        continue
    elif i == 2:
        memo[i] = stairs[i] + stairs[i-1]
        continue

    memo[i] = max(memo[i-3]+stairs[i-1]+stairs[i], memo[i-2]+stairs[i])

print(memo[-1])