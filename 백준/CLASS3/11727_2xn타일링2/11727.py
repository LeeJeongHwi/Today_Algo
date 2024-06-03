from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

memo = [0 for _ in range(1001)]

memo[1] = 1
memo[2] = 3
memo[3] = 5

for i in range(4, n+1):
    memo[i] = (memo[i-1]*2 - memo[i-3]*2) + (memo[i-2])

print(memo[n]%10007) 