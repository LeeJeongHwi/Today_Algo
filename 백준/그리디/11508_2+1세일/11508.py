from sys import stdin
from collections import deque
stdin = open('input.txt')

N = int(stdin.readline())

# 유제품 3개를 한번에 산다면 그중에서 가장 싼 것은 무료로 지불, 두개의 제품 가격만 지불
# 한번에 3개의 유제품을 사는게 아니라면 할인 없이 정가 지출
# 10 9 8 7 있으면? (10 7 8) , (9 ) -> 큰거하나 , 작은거 2개 이런순으로 진행

def solution(N, prices):
    answer = 0
    while prices:
        first = prices.popleft() # 비싼거
        if prices:
            second = prices.popleft() # 2번째로 싼거
        else: # 비어있다면
            answer += first
            continue
        if prices:
            third = prices.popleft() # 제일 싼거
        else: # 비어있다면
            answer += (first + second)
            continue
        
        # 3개 묶음이 있는 경우
        answer += (first + second)

    return answer
        
inputs = [int(stdin.readline()) for _ in range(N)]
inputs.sort(reverse=True)
prices = deque(inputs)
print(solution(N, prices))