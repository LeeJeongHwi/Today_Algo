from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())
sizes = list(map(int,stdin.readline().split()))
T, P = map(int,stdin.readline().split()) # T셔츠와 P엔 묶음

t_group = 0
for s in sizes:
    if s <= T:
        if s != 0:
            t_group += 1
    else:
        t_group += (s//T if s%T == 0 else s//T+1)

print(t_group)
print(n//P, n%P)
