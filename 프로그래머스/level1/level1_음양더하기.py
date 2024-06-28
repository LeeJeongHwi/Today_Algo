def solution(absolutes, signs):
    answer=0
    for num, b in zip(absolutes, signs):
        if b:
            answer+=num
        else:
            answer-=num
    return answer
    