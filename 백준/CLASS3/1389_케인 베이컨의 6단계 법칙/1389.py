from sys import stdin
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

graphs = [[float("inf") for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y = map(int,stdin.readline().split())
    graphs[x-1][y-1] = 1
    graphs[y-1][x-1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graphs[i][j] = 0

def floyd_Warshall(graphs):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graphs[i][j] = min(graphs[i][j], graphs[i][k]+graphs[k][j])

    min_i = min_g = float("inf")
    for i, g in enumerate(graphs):
        if min_g > sum(g):
            min_i = i
            min_g = sum(g)
    
    return min_i+1


print(floyd_Warshall(graphs))

