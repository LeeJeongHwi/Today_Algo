def solution(n, left, right):
    # 근데 채우지 않고 얻어내야함
    # n=4에서 2~5 라고 했을 때 i,j를 각각 구해야함

    # 2,3,4,5,6 이렇게 흘러가는데,
    # 0번째 인덱스는 행마다의 i가 나와야함
    # 1번쨰 인덱스는 열마다의 i가 나와야함
    # [1,3][1,4] [2,1][2,2][2,3]
    
    answers = []
    for i in range(left, right+1):
        answers.append(max([i//n+1,i%n+1]))
    
    return answers

print(solution(4,2,6))