from sys import stdin
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

# 대칭이 필요한 mino : L S
# 대칭 회전이 필요없는 mino : Square
# 회전 하나만 필요한 mino : I
# 4방향 회전만 필요한 mino : T

def rotate(mino, y, x, rot_c):
    cos_90 = 0
    sin_90 = 1
    transformed_coord = []
    for c in range(rot_c):
        coords = [] 
        for i, cor in enumerate(mino):
            x_ = (cor[1]-x) * cos_90 - (cor[0]-y) * sin_90 + x
            y_ = (cor[1]-x) * sin_90 - (cor[0]-y) * cos_90 + y
            coords.append([y_,x_])
            mino[i] = [y_,x_]
        transformed_coord.append(coords)
    return transformed_coord

def reverse(mino):
    return [[y,-x] for y,x in mino]

minos = [[[0,0],[0,1],[0,2],[0,3]], # I
         [[0,0],[0,1],[1,1],[1,0]], # SQ
         [[0,0],[0,1],[0,-1],[1,0]], # T
         [[0,0],[1,0],[1,1],[2,1]], # S
         [[0,0],[1,0],[2,0],[2,1]]] # L


def generate_forms():
    all_Form = []

    #로테이션 데이터 추가
    tI = rotate(minos[0],0,0,2)
    tT = rotate(minos[2],0,0,4)
    tS = rotate(minos[3],0,0,4)
    tL = rotate(minos[4],0,0,4)
    rS = reverse(minos[3])
    rL = reverse(minos[4])
    trS = rotate(rS,0,0,4)
    trL = rotate(rL,0,0,4)

    for coords in [tI,tT,tS,tL,trS,trL]:
        for coord in coords:
            all_Form.append(coord)
    all_Form.append(minos[1])
    # from pprint import pprint
    # pprint(all_Form)
    return all_Form

forms = generate_forms()

max_sums = 0
for i in range(n):
    for j in range(m):
        for form in forms:
            y1,x1 = form[0][0]+i, form[0][1]+j
            y2,x2 = form[1][0]+i, form[1][1]+j
            y3,x3 = form[2][0]+i, form[2][1]+j
            y4,x4 = form[3][0]+i, form[3][1]+j
            
            if (0 <= y1 < n and 0 <= x1 < m) and (0 <= y2 < n and 0 <= x2 < m) and (0 <= y3 < n and 0 <= x3 < m) and (0 <= y4 < n and 0 <= x4 < m):
                # print(f"[{y1,x1}],[{y2,x2}],[{y3,x3}],[{y4,x4}]",maps[y1][x1] + maps[y2][x2] + maps[y3][x3] + maps[y4][x4])
                max_sums = max(max_sums, maps[y1][x1] + maps[y2][x2] + maps[y3][x3] + maps[y4][x4])
print(max_sums)
                