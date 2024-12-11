def solution(dirs):
    maps = [[0 for _ in range(11)] for _ in range(11)]
    
    #init
    x, y = 5, 5 #x좌표, y좌표
    ans = set()

    for op in dirs:
        if op == "U": # Up, y좌표 -1
            nx, ny = x, y-1

        elif op == "L": # left
            nx, ny = x-1, y
                
        elif op == "R": # Right
            nx, ny = x+1, y

        elif op == "D": # Down
            nx, ny = x, y+1

        if (0 <= nx < 11) and (0 <= ny < 11):
            ans.add((x,y,nx,ny))
            ans.add((nx,ny,x,y))
            x,y = nx,ny

    return len(ans)//2