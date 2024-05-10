from sys import stdin
stdin = open('input.txt')

a, b = sorted(map(int,stdin.readline().split()), reverse=True)

def mod(a,b):
    return a//b, a%b

GCD,LBS = 0,0

while True:
    if mo