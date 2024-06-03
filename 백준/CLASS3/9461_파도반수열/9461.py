from sys import stdin
stdin = open('input.txt')
t = int(stdin.readline())

def sequence(n):
    
    memo = [0 for _ in range(101)]
    memo[1]=1
    memo[2]=1
    memo[3]=1

    for i in range(4, n+1):
        memo[i] = memo[i-2]+memo[i-3]
    
    print(memo[n])

for _ in range(t):
    n = int(stdin.readline())
    sequence(n)
