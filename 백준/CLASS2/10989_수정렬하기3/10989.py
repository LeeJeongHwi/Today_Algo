from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

# 삽입정렬 해보자
num_list = [int(stdin.readline()) for _ in range(n)]

for i in sorted(num_list):
    print(i)