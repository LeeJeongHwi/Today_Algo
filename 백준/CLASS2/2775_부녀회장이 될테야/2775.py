from sys import stdin
stdin = open('input.txt')

T = int(stdin.readline())

# 0층에 i호 에는 i명이 산다.
# a층의 b호에 사려면, 자신의 아래 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 데려와야함


def ans():
    k_floor = int(stdin.readline())
    number = int(stdin.readline())
    
    memo = [[0 for _ in range(number)] for _ in range(k_floor+1)]

    # 0 Floor
    for i in range(number):
        memo[0][i] = i+1

    # Dynamic Programming
    for i in range(1, k_floor+1):
        for j in range(number):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]

    print(memo[k_floor][number-1])


for _ in range(T):
    ans()