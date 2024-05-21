from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())
coord = [list(map(int,stdin.readline().split())) for _ in range(n)]
coord.sort(key=lambda x: (x[1],x[0]))
for x,y in coord:
    print(x, y)