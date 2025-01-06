from sys import stdin
stdin = open('input.txt')

N, X = map(int,stdin.readline().split())

ans = []
for num in list(map(int,stdin.readline().split())):
    if num < X:
        ans.append(f"{num}")

print(" ".join(ans))