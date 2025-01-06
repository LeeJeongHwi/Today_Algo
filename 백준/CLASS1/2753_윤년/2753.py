from sys import stdin
stdin = open('input.txt')

n = int(stdin.readline())
if n%4 == 0:
    if n%100 != 0 or n%400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)