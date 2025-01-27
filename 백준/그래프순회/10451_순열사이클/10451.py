from sys import stdin
stdin = open('input.txt')

T = int(stdin.readline())

def dfs(start, num, memo, graph):
    memo[num] = 1
    if memo[graph[num]] == 0:
        return dfs(start, graph[num], memo, graph)
    else:
        if graph[num] == start:
            return True
        else:
            return False


for _ in range(T):
    N = int(stdin.readline())
    graph = {i+1: v for i,v in enumerate(list(map(int,stdin.readline().split())))}
    memo = [0 for _ in range(N+1)]
    st = []
    count = 0
    for i in range(1, N+1):
        if memo[i] == 0:
            if dfs(i, i, memo, graph):
                count += 1
    print(count)
