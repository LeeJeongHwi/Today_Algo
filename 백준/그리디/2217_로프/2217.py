from sys import stdin
stdin = open('input.txt')

N = int(stdin.readline())

# k 로프 사용, 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k만큼 중량이 걸림
# 로프들을 이용해서 들어올릴 수 있는 물체의 최대 중량
# 임의의 로프만 사용가능
# N개의 로프, K 중량 입력
"""
10, 15가 들어왔을 때, 15만 쓰는경우 15kg 중량, 10만 쓰는 경우 10kg 중량, 15와 10을 둘다 쓰는 경우 10에 맞춘 10+10 -> 20
- 수 정렬 (역순)
- 0번째부터 돌고, 
- 그 다음 수가 들어오면, 그 수 * i 만큼이 들 수 있는 최대 용량임, 다 돌고나면 max값 return
"""

def solution(ropes):
    max_weight = 0
    for i, r in enumerate(ropes):
        m_w = r * (i+1)
        if max_weight < m_w:
            max_weight = m_w
    return max_weight

ropes = [int(stdin.readline()) for _ in range(N)]
ropes.sort(reverse=True)

print(solution(ropes))