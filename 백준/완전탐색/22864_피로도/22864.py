from sys import stdin
stdin = open('input.txt')

A, B, C, M = map(int,stdin.readline().split())

# A만큼 쌓이고, B만큼 처리, C만큼 줄어듬, M을 안넘기게하려함, 하루에 최대 얼마나 할 수 있는가, 하루는 24시간
# 5 3 2 | 10

def solution(A, B, C, M):
    hp = 0
    task = 0
    day = 24
    while day > 0:
        if hp + A > M:
            #rest 필요
            hp -= C
            if hp < 0:
                hp = 0
        else:
            hp += A
            task += B

        day -= 1

    return task
    
print(solution(A, B, C, M))
print(solution(10, 5, 1, 10))
print(solution(5, 3, 2, 10))