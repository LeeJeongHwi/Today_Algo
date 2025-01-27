from sys import stdin
stdin = open('input.txt')

n, q = map(int,stdin.readline().split())

nlist = [0]+list(map(int,stdin.readline().split()))

for _ in range(q):
    query = list(map(int,stdin.readline().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        print(sum(nlist[a:b+1]))
        nlist[a], nlist[b] = nlist[b], nlist[a]

    elif query[0] == 2:
        ab = sum(nlist[query[1]:query[2]+1])
        cd = sum(nlist[query[3]:query[4]+1])
        print(ab - cd)