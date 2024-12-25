from sys import stdin
stdin = open('input.txt')

N = int(stdin.readline())

# 줄 돈 - (등수 -1) = 팁
"""
tip을 가장 큰 순으로 적게 -되서 받아야 가장 많이 가져갈 수 있음
따라서, tips를 정렬하고 계산식에 넣는다.
"""

def solution(N, tips):
    answer = 0
    for i, t in enumerate(tips):
        tip = t-(i)
        if tip < 0: # 그 뒤로는 어차피 음수가 되기 때문
            return answer
        answer+=tip
    return answer

tips = [int(stdin.readline()) for _ in range(N)]
tips.sort(reverse=True)
print(solution(N, tips))

"""
solved : 76ms
"""