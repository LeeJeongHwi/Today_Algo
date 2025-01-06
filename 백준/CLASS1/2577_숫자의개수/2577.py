from sys import stdin
stdin = open('input.txt')

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

num = str(A*B*C)
numbers = [0 for _ in range(10)]

for n in num:
    numbers[int(n)] += 1

for n in numbers:
    print(n)