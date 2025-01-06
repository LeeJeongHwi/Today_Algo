from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())

for i in range(1,10):
    print(f"{n} * {i} = {n*i}")