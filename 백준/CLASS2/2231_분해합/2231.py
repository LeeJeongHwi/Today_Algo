stdin = open("input.txt","r")

from sys import stdin

N = stdin.readline().rstrip()


for i in range(int(N)):
    numbers = str(i)
    generator = sum(list(map(int,numbers))) + int(numbers)
    if generator == int(N):
        print(i)
        break
else:
    print(0)
    

# 다른 풀이 참조
"""
N - (9 * 자릿수) , N 까지 보면 된다
왜냐면 9 * 자릿수 만큼 뺀 것보다 작은 수는 생성자가 될 수 없기 때문이다.
식으로 보면 다음과 같다.

N = k1 + k2 + k3 + k4 + K
N - (k1 + k2 + k3 + k4) = K
각 자릿수가 9인 경우가 가장 작은수이고, 그것보다 작은수가 나올 수가 없기 때문에
저때부터 for문을 돌리면 된다.
"""