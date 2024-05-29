from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

timep = list(map(int,stdin.readline().split()))

timep.sort()

ans = 0

for i in range(1,n+1):
    ans += sum(timep[:i])
    
print(ans)