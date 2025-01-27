from collections import deque
from sys import stdin
stdin = open('input.txt')

R, C, N = map(int,stdin.readline().split())
# R 세로, C 가로, N초

def explode(maps, bomb):
    direct = [[1,0], [0,1], [-1,0], [0,-1]]
    while bomb:
        now_y, now_x = bomb.popleft()
        maps[now_y][now_x] = "."
        for dy, dx in direct:
            ny = dy + now_y
            nx = dx + now_x
            if 0 <= ny < R and 0 <= nx < C:
                maps[ny][nx] = "." # 터트림


def put_bomb(maps):
    for i in range(R):
        for j in range(C):
            if maps[i][j] == ".":
                maps[i][j] = "O"

def print_map(maps):
    for map in maps:
        print("".join(map))

def check_bomb(maps, bomb):
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "O":
                bomb.append([i, j])

if __name__ == "__main__":
    maps = []
    bomb = deque()
    time = 1
    for i in range(R): # map init
        row = []
        for j, s in enumerate(stdin.readline().rstrip()):
            if s == "O":
                row.append(s)
                bomb.append([i, j]) # 3초에 터짐
            else:
                row.append(s)
        maps.append(row)
    
    while time < N:
        if time % 2 == 0:
            explode(maps, bomb)
            check_bomb(maps,bomb)
        elif time % 2 == 1:
            put_bomb(maps)

        time+=1
    
    print_map(maps)
    

    

    





        
# . 은 평지, o는 폭탄
# N초 후 바닥 상황을 표시

