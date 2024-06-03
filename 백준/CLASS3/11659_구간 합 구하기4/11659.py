from sys import stdin
stdin = open('input.txt')
n, m = map(int,stdin.readline().split())
num_list = list(map(int,stdin.readline().split()))

for i in range(1, n):
    num_list[i] = num_list[i] + num_list[i-1]

# print(num_list)

def get_Subsum(start, end):
    if start == 1:
        print(num_list[end-1])
    else:
        print(num_list[end-1] - num_list[start-2])

for _ in range(m):
    i, j = map(int,stdin.readline().split())
    get_Subsum(i, j)