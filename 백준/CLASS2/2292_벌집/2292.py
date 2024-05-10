"""
1 -> 6 -> 12 -> 18 -> 24 -> 30 -> ... 
1 -> (2 ~ 7) -> (8 ~ 19) -> (20 ~ 37) -> (38 ~ 61) -> (62 ~ 91)

레이어는 6의 배수 개수마다 쌓임
만약에 78 이라고 했을때 6번째 레이어에 존재함
그래서 -1 하고 해보자

0 -> (1 ~ 6) -> (7 ~ 18) -> (19 ~ 36) -> (37 ~ 60) -> (61 ~ 90) ...

1 -> 3 -> 6 -> 10 -> 15
개수를 세자
최대 166,666,666
"""

from sys import stdin

stdin = open("input.txt","r")
n = int(stdin.readline().rstrip())

start_num=2
end_num=7
i = 2
layer=1
while True:
    # print(start_num, end_num, 6*i)
    if n == 1:
        print(1)
        break
    if (start_num <= n <= end_num):
        print(layer+1)
        break
    start_num = end_num + 1
    end_num = start_num + (6*i) - 1
    i+=1
    layer+=1

# 사실 간단한 문제였다..
# 그냥 (6*i) 만큼 계속 Size에 더해주면서 걔보다 커지면 break 시키고 i를 출력하면 되는 거였음
