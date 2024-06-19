from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())


maps = [list(map(str,stdin.readline().split())) for _ in range(n)]

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        # maps[i][j] = i에서 j까지 가는 길
        for j in range(n):
            if maps[i][k] == "1" and maps[k][j] == "1":
                maps[i][j] = "1"

for v in maps:
    print(" ".join(v))


# DFS로 풀 수 있다. (BFS나)