# https://aia1235.tistory.com/37
from sys import stdin
stdin = open('input.txt')
n = int(stdin.readline())


# year = 10 * p + 3 = 12 * q + 9 를 만족함 (p,q는 자연수)
# year-3은 10으로 나누어떨어지고, year-9는 12로 나누어떨어진다.
def calander(M,N,x,y):
    year = x
    while year <= M * N:
        if (year-x) % M == 0 and (year-y) % N == 0:
            return year
        
        year += M
    
    return -1

for _ in range(n):
    m, n, x, y = map(int,stdin.readline().split())
    print(calander(m,n,x,y))
    