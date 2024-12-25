from sys import stdin
stdin = open('input.txt')

n, k = map(int,stdin.readline().split())

coins = [int(stdin.readline()) for _ in range(n)]

def solution(k, coins):
    coins.sort(reverse=True)
    answer = 0
    for coin in coins:
        if k == 0:
            return answer
        if k//coin == 0: # 나눌 수 없는 경우
            continue
        else:
            answer += (k // coin)
            k = k % coin

    return answer

print(solution(k, coins))