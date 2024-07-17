from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
min_visit = [[0]*3 for _ in range(2)]
max_visit = [[0]*3 for _ in range(2)]

def get_minmax():
    for i in range(1,n+1):
        max_visit[i%2][0] = max(max_visit[not i%2][0] + maps[i-1][0], max_visit[not i%2][1] + maps[i-1][0])
        max_visit[i%2][1] = max(max_visit[not i%2][0] + maps[i-1][1], max_visit[not i%2][1] + maps[i-1][1], max_visit[not i%2][2] + maps[i-1][1])
        max_visit[i%2][2] = max(max_visit[not i%2][1] + maps[i-1][2], max_visit[not i%2][2] + maps[i-1][2])
        min_visit[i%2][0] = min(min_visit[not i%2][0] + maps[i-1][0], min_visit[not i%2][1] + maps[i-1][0])
        min_visit[i%2][1] = min(min_visit[not i%2][0] + maps[i-1][1], min_visit[not i%2][1] + maps[i-1][1], min_visit[not i%2][2] + maps[i-1][1])
        min_visit[i%2][2] = min(min_visit[not i%2][1] + maps[i-1][2], min_visit[not i%2][2] + maps[i-1][2])
    
    print(max(max_visit[i%2]), min(min_visit[i%2]))

get_minmax()