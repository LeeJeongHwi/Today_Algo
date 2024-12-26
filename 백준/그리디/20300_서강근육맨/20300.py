from sys import stdin
stdin = open('input.txt')

N = int(stdin.readline())

# 근손실 정도를 나타내는 정수 t1 ~ tN
# 운동기구의 개수를 나타내는 정수 N
# 근손실 정도 M의 최솟값을 구하는 문제

# 홀수면 1개가 무조건 남음
# 짝수면 남지 않음
def solution(N, loss):
    loss.sort()
    left = 0
    right = N-1
    M = 0
    if N%2 != 0 : # 홀수인 경우 무조건 한개만 쓰는 경우가 존재 -> 가장 큰 값을 쓴다면?
        M = loss.pop() # 가장 큰 값
        right -= 1

    while True:
        if left > right:
            break
        M = max(M, loss[left] + loss[right])
        left+=1
        right-=1
    
    return M


losses = list(map(int,stdin.readline().split()))
print(solution(N, losses))
