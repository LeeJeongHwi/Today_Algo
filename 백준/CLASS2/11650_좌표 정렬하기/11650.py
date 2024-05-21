from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())
coord = sorted([list(map(int, stdin.readline().split())) for _ in range(n)],key=lambda x:(x[0],x[1]))
for x,y in coord:
    print(x,y)
