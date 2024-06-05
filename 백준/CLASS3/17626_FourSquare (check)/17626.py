from sys import stdin
from math import sqrt
# https://rujang.tistory.com/entry/%EB%B0%B1%EC%A4%80-17626%EB%B2%88-Four-Squares-CC
stdin = open('input.txt')
n = int(stdin.readline())

memo = [0 for _ in range(50001)]

for i in range(1,n+1):
    
    memo[i] = memo[i-1] + 1
    j = 1
    while j*j<=i:
        memo[i] = min(memo[i], memo[i-j*j] + 1)
        j += 1

print(memo[n])