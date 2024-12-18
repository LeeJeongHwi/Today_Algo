def solution(arr):
    answer = []
    for x in arr:
        if not answer:
            answer.append(x)
            continue
        if answer[-1] == x:
            continue
        answer.append(x)
    return answer