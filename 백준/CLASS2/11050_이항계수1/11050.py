from sys import stdin
from math import factorial
stdin = open('input.txt')

# 이항계수란, 원하는 개수만큼 순서없이 뽑는 조합의 가짓수
# C_k = n! / (n-k)!k!

n, k = map(int, stdin.readline().split())
print(int(factorial(n)/(factorial(n-k)*factorial(k))))