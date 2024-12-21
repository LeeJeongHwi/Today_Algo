from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

def solution(n):
# 2원 / 5원
    count5 = n//5
    while count5 >= 0:
        k = n
        count_all = 0
        # 5원의 최대 개수로 나눈 값
        count_all += count5
        rem5 = k - (count5 * 5)
        if rem5 != 0: # 5원으로 해도 다 안될 때
            # 2원으로 처리
            rem2 = rem5 % 2
            if rem2 == 0: # 다 처리 가능
                count_all += (rem5 // 2)
                return count_all
            count5-=1
        else:
            return count_all
    return -1

print(solution(n))