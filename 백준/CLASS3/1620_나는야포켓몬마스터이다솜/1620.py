from sys import stdin
stdin = open('input.txt')


n, m = map(int,stdin.readline().split())

pokDict = {}

for i in range(1,n+1):
    name = stdin.readline().rstrip()
    pokDict[str(i)] = name
    pokDict[name] = str(i)

for _ in range(m):
    name = stdin.readline().rstrip()
    print(pokDict[name])