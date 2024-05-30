from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

memo = [0 for _ in range(n+1)]

# 아래 풀이는 Bottom up 방식으로 해결한 것
# Top-down 방식은 재귀로 처리하면됨
#init
memo[1] = 0

for i in range(2, n+1):
    if i == 2 or i == 3:
        memo[i] = 1
        continue

    min_num = float("inf")

    if i%3 == 0:
        min_num = min(min_num, memo[i//3]+1)
    if i%2 == 0:
        min_num = min(min_num, memo[i//2]+1)
    
    min_num = min(min_num, memo[i-1]+1)

    memo[i] = min_num

print(memo[n])
    