def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        prior = 1
        for j in range(2, i+1):
            if i % j == 0:
                prior += 1
        if prior % 2 == 0:
            answer += i
        else:
            answer -= i
        
        
    return answer