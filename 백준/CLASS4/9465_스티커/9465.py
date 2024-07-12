from sys import stdin
stdin = open('input.txt')
t = int(stdin.readline())

def get_max(n, stickers):
    # 변과 공유하는 스티커 -> 4방위
    dp = [[0 for _ in range(n)] for _ in range(2)]

    for i in range(n):
        if i == 0:
            dp[0][0] = stickers[0][0]
            dp[1][0] = stickers[1][0]
        elif i == 1:
            dp[0][1] = dp[1][0] + stickers[0][1]
            dp[1][1] = dp[0][0] + stickers[1][1]
        else:
            # [0][i-1] 번째 선택한 경우, [1][i-1]번째 선택한 경우, 이전 스티커 선택 안한 경우([i-2][0],[i-2][1] 중 큰 수치 선택)
            dp[0][i] = max(dp[1][i-1]+stickers[0][i], dp[0][i-2]+stickers[0][i], dp[1][i-2]+stickers[0][i])
            dp[1][i] = max(dp[0][i-1]+stickers[1][i], dp[0][i-2]+stickers[1][i], dp[1][i-2]+stickers[1][i])
            
    print(max(dp[0][n-1],dp[1][n-1]))
    
for _ in range(t):
    n = int(stdin.readline())
    stickers = [list(map(int,stdin.readline().split())) for _ in range(2)]
    get_max(n, stickers)



