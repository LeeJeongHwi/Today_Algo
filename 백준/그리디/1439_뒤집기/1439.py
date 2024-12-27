from sys import stdin
stdin = open('input.txt')

numbers = stdin.readline().rstrip()

def solution(numbers):
    reverse_count = {"1":0, "0":0}
    N = len(numbers)
    for i in range(N):
        if i < N-1:
            if numbers[i] == numbers[i+1]:
                continue
            else:
                reverse_count[numbers[i]] += 1
        else:
            reverse_count[numbers[i]] += 1
    return min(reverse_count.values())

print(solution(numbers))

            
