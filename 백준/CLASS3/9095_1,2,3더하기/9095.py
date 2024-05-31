from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

def solve(num):
    memo = [0 for _ in range(num+1)]
    # memo[n-3] 인경우, memo[n-2] 인경우, memo[n-1] 인경우
    for i in range(1, num+1):
        if i == 1:
            memo[i] = 1
            continue
        elif i == 2:
            memo[i] = 2
            continue
        elif i == 3:
            memo[i] = 4
            continue
        
        memo[i] = memo[i-3]+memo[i-2]+memo[i-1]
    
    print(memo[num])


for _ in range(n):
    num = int(stdin.readline())
    solve(num)