from sys import stdin
stdin = open('input.txt')

max_i = 0
max_v = 0

for i in range(9):
    n = int(stdin.readline())
    if max_v < n:
        max_i = i+1
        max_v = n

print(max_v)
print(max_i)