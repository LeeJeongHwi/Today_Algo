from sys import stdin
stdin = open('input.txt')

# remove = 2 sec
# put = 1 sec

n, m, b = map(int,stdin.readline().split())

maps = []
min_height = float("inf")
max_height = -1

for _ in range(n):
    line = list(map(int,stdin.readline().split()))
    maps.append(line)
    min_height = min(min_height, min(line))
    max_height = max(max_height, max(line))

def minecraft(bag, height):
    time = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] < height: # 목표 높이보다 낮으면 설치해야함
                diff = height - maps[i][j]
                bag -= diff
                time += (diff*1)
            else: # 목표 높이보다 높으면 깎아야함
                diff = maps[i][j] - height
                bag += diff
                time += (diff*2)
    
    # print("target_hieght:",height)
    # print(time, bag)

    if bag < 0:
        return -1
    return time

import copy

max_h = -1
min_t = float("inf")

for t_h in range(min_height, max_height+1):
    bag = copy.deepcopy(b)
    time = minecraft(bag, t_h)
    if time == -1:
        continue
    
    if (max_h < t_h) and (min_t >= time):
        max_h = t_h
        min_t = time

print(min_t, max_h)