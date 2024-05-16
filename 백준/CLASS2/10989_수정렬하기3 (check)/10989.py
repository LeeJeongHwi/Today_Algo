from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

# 전체 배열을 다 담는순간부터 메모리 에러남, 계수 정렬이라는 걸 사용해야함 사용해야함
# 수가 10000으로 지정되어있음
cnt = [0]*10001

for _ in range(n):
    cnt[int(stdin.readline())] += 1

for i, k in enumerate(cnt):
    for _ in range(k):
        print(i)

