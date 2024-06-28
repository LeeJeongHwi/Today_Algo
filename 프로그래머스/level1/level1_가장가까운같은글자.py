def solution(s):
    answer = []
    
    alpha_dict = {}
    
    for i, alpha in enumerate(s):
        if alpha not in alpha_dict:
            alpha_dict[alpha] = i
            answer.append(-1)
        else:
            answer.append(i - alpha_dict[alpha])
            alpha_dict[alpha] = i
    
    
    return answer