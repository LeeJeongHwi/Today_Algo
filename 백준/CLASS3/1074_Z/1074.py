from sys import stdin
stdin = open('input.txt')
n, r, c = map(int,stdin.readline().split())
num = 0


# maps = [[0 for _ in range(2**n)] for _ in range(2**n)]

# map을 굳이 안써줘도된다, 여기서 map을 구성하는 시간부터 이미 시간초과가 난다..
# 이것만 해결했으면 됐는데 아ㅏㅏㅏㅏㅏㅏㅏ

def divide(sy, sx, size):
    global num, maps

    # print("sy",sy, "sx",sx, "size", size)

    if size == 1:
        if sy == r and sx == c:
            print(num)
        num+=1
        return
    
    n_size = size//2

    if (sy <= r < sy + size) and (sx <= c < sx + size):
        divide(sy, sx, n_size) # 2사분면
        divide(sy, sx + n_size, n_size) # 1사분면
        divide(sy + n_size, sx, n_size) # 3사분면
        divide(sy + n_size, sx + n_size, n_size) # 4사분면

    else:
        num += size**2
    
divide(0,0, 2**n)
