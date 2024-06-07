from sys import stdin
stdin = open("input.txt","r")

n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

blue_count = 0
white_count = 0
def check_maps(sx,ex,sy,ey):
    global blue_count, white_count
    start = maps[sy][sx]
    # print(sx, sy, start)
    for i in range(sy,ey):
        for j in range(sx,ex):
            # print(maps[i][j], end=" ")
            if maps[i][j] != start: # 하나라도 다르면 False
                return False
        # print()
    if start == 1:
        blue_count+=1
        return True
    else:
        white_count+=1
        return True

# 색종이를 4분할을 1개만 남을 때 까지 분할해야함
# 지금 검사하고 있는 영역이 모두 1이거나 0이 되어야만 return하고 count함
# 분할하는 부분은 현재 길이의 N/2 만큼

def divide(sx, ex, sy, ey):
    global blue_count, white_count
    # print(f"X {sx}, {ex} | Y {sy}, {ey}")
    # 종료 조건 sx == ex-1 일때?
    if sx == ex-1 and sy == ey-1:
        if maps[sy][sx] == 1:
            blue_count+=1
            return
        else:
            white_count+=1
            return
    if check_maps(sx,ex,sy,ey):
        return
    else:
        x_mid = ((ex-sx)//2 + sx)
        y_mid = ((ey-sy)//2 + sy)
        divide(sx, x_mid, sy, y_mid) # X: 0, 2/N 까지 Y: 0, N/2 까지
        divide(x_mid, ex, sy, y_mid) # X: N/2, N 까지 Y: 0, N/2 까지
        divide(sx, x_mid, y_mid, ey) # X: 0, N/2 까지 Y: N/2, N 까지
        divide(x_mid, ex, y_mid, ey) # X: N/2, N 까지 Y: N/2, N 까지

# Answer : "잘라진 색종이의 개수" , "색칠된 영역의 개수"

divide(0, n , 0, n)
print(white_count, blue_count)