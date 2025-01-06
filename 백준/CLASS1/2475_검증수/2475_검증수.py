from sys import stdin
stdin = open('input.txt')

def pows(x):
    return int(x)**2

verifyCode = sum(list(map(pows,stdin.readline().split())))%10
print(verifyCode)

