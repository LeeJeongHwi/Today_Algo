from sys import stdin
stdin = open('input.txt')
A, B, C = map(int,stdin.readline().split())

#2,147,486,647 이하의 자연수
# 분할정복을 이용한 거듭제곱임

def power(a, n):
    result = 1
    while n:
        if n & 1 :
            result *= a

        a *= a
        a %= C
        n = n >> 1
        
    return result

print(power(A,B)%C)