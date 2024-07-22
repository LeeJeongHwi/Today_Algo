from sys import stdin
stdin = open('input.txt')
n, k = map(int,stdin.readline().split())
# k 무게, n 수

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
items = [[0,0]]
for _ in range(n):
    items.append(list(map(int,stdin.readline().split())))


# 열 마다 무게를 의미

for i in range(1,n+1): # i 는 현재 아이템
    for j in range(1,k+1): # j 는 현재 가방 무게
        
        # dp[i-1][j] : i번째 물건을 안넣은 것 (무게 유지)
        # dp[i-1][j-items[i][0]]+items[i][1] : 이전 상태에서 i번째 물건을 넣은 상황
        # j-itesm[i][0] : 현재 배낭무게에서 i번째를 넣어서 무게만큼 뺀거고 가치를 더함

        if j >= items[i][0]: # 현재 배낭의 무게보다 아이템의 무게가 더 작을때
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-items[i][0]]+items[i][1])
        else:
            dp[i][j] = dp[i-1][j] # 배낭의 무게보다 더 크면 넣을수가 없으니 패쓰

# for d in dp:
#     print(d)
print(dp[n][k])