from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

for _ in range(n):
    p, strs = stdin.readline().split()
    p = int(p)

    for s in strs:
        print(s*p, end="")
    print()