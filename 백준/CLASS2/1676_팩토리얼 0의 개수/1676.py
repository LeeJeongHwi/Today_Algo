from sys import stdin
from math import factorial
stdin = open('input.txt')

n = int(stdin.readline())
facto = str(factorial(n))

i = 1
while True:
    if facto[-i] != "0":
        break
    i += 1
print(i-1)