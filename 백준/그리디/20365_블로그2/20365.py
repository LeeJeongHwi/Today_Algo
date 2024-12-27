from sys import stdin
stdin = open('input.txt')

N = int(stdin.readline())

# 해결한 경우 파란색, 해결하지 못한 경우 빨간색
# BBRBRBBR 이 있다면, BBBBBBB를 1~7번까지로 칠하고 BBRBRBBR로 R을 채우기
# 어떻게 해야할지?
"""
- 각 색의 count를 하고 for문으로 돌면서 이전거랑 같은 색이면 pass, 다른 색이면 count+1
"""
def solution(N, problems):
    color_count = {"R":1, "B":1}
    for i in range(N):
        if i < N-1:
            if problems[i] == problems[i+1]:
                continue
            else:
                color_count[problems[i]] += 1
        else:
            color_count[problems[i]] += 1
    return min(color_count.values())

problems = stdin.readline().rstrip()
# solution(N, problems)
print(solution(6, "BRBBRR"))
print(solution(6, "BRRRRB"))

""" 1등 풀이
n = int(input())

x = input()
# 맨처음 파랑을 다 칠했을 때
if x[-1] == "R":
    B_cnt = 2
else:
    B_cnt = 1

B_cnt += x.count("RB")

#맨처음 빨강을 다 칠했을 때

if x [-1] == "B":
    R_cnt = 2
else:
    R_cnt = 1

R_cnt += x.count("BR")

print(min(R_cnt,B_cnt))
"""