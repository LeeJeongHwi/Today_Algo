from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
person = [list(map(int,stdin.readline().split())) for _ in range(n)]


for i in range(n):
    x_a, y_a = person[i][0], person[i][1]
    rank = 1
    for j in range(n):
        if i == j:
            continue

        x_b, y_b = person[j][0], person[j][1]

        if (x_a < x_b and y_a < y_b):
            rank+=1

    print(rank)
