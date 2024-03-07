from sys import stdin
import sys
from copy import deepcopy
from pprint import pprint


# Brute Force로 푼 경우임

stdin = open("종만북/보글게임/input.txt","r")
sys.setrecursionlimit(100000)

tc = int(stdin.readline())
position = [[1,0],[-1,0],[0,1],[0,-1], [1,1],[1,-1],[-1,1],[-1,-1]]

def search(maps, x, y, voca):
    if maps[x][y] != voca[0]:
        return False
    if len(voca) == 1:
        return True

    for dx, dy in position:
        nx = x+dx
        ny = y+dy
        if (0<=nx<=4 and 0<=ny<=4):
            if search(maps, nx, ny, voca[1:]):
                return True
            
    return False

def solution(maps, voca):
    for i in range(5):
        for j in range(5):
            if search(maps, i, j, voca):
                return True
            
for c in range(tc):
    maps = []
    for i in range(5):
        lines = stdin.readline().rstrip()
        mline = []
        for j in range(5):
            mline.append(lines[j])
        maps.append(mline)
    n = int(stdin.readline())
    for _ in range(n):
        voca = stdin.readline().rstrip()
        if solution(maps, voca):
            print(voca, "YES")
        else:
            print(voca, "NO")
    
    