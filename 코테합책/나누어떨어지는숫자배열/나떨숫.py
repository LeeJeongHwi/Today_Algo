def solution(arr, divisor):
    answer = [x for x in sorted(arr) if x%divisor==0]
    if not answer:
        return [-1]
    return answer