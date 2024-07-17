from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())

min_visit = [[0]*3 for _ in range(2)]
max_visit = [[0]*3 for _ in range(2)]

# Maps를 설정해서도 안되고, 2단배열로 설정하는것도 안된다..?

def get_minmax():
    for i in range(1,n+1):
        map1, map2, map3 = map(int,stdin.readline().split())
        max_visit[i%2][0] = max(max_visit[not i%2][0] + map1, max_visit[not i%2][1] + map1)
        max_visit[i%2][1] = max(max_visit[not i%2][0] + map2, max_visit[not i%2][1] + map2, max_visit[not i%2][2] + map2)
        max_visit[i%2][2] = max(max_visit[not i%2][1] + map3, max_visit[not i%2][2] + map3)
        min_visit[i%2][0] = min(min_visit[not i%2][0] + map1, min_visit[not i%2][1] + map1)
        min_visit[i%2][1] = min(min_visit[not i%2][0] + map2, min_visit[not i%2][1] + map2, min_visit[not i%2][2] + map2)
        min_visit[i%2][2] = min(min_visit[not i%2][1] + map3, min_visit[not i%2][2] + map3)
    
    print(max(max_visit[i%2]), min(min_visit[i%2]))

get_minmax()